import math
from cmath import sqrt
from dataclasses import dataclass
from enum import Enum
from io import BytesIO
import pandas as pd
import requests
import json
from typing import List, Optional, Dict, Any
from wordcloud import WordCloud
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import gensim
from gensim.utils import simple_preprocess

from Utils.Enums import RomanianParty, ManifestoCodes
from Utils.UtilityFunctions import preprocess_text, find_word_in_manifestos
from analysis.HandCodingAnalysis import calculate_hand_coded_similarity, analyze_party_codes
from analysis.SentimentAnalysis import print_sentiment_analysis
from analysis.TextAnalysisTFIDF import analyze_word_commonality, find_party_specific_vocabulary
from analysis.TopicModelin import ManifestoTopicModeling
from api.ManifestoApi import ManifestoAPI


def main():
	api_key = "147c9bb7aefe93dc971088e6210d8f46"
	api = ManifestoAPI(api_key)

	target_manifestos = [
		"93223_201612",
		# "93420_201612", # ALDE prea mic, adauga noise degeaba
		"93430_201612",
		"93440_201612",
		"93540_201612",
		"93951_201612"
	]

	try:
		manifesto_data = api.fetch_manifestos(target_manifestos)

		manifesto_corpus = []
		for manifesto in manifesto_data:
			print("\nManifesto Details:")
			print(f"Title: {manifesto.metadata.title}")
			print(f"Party: {RomanianParty.get_name(manifesto.metadata.party_id)}")
			print(f"Election Date: {manifesto.metadata.election_date}")
			print(f"Language: {manifesto.metadata.language}")
			print(f"Number of text items: {len(manifesto.text_items)}")

			print("\nAll the text:")
			full_text = ''
			for item in manifesto.text_items:
				full_text = full_text + item.text + ' '
			number_of_words = len(full_text.split())
			print(f"Number of words before preprocess: {number_of_words}")
			full_text = preprocess_text(full_text.strip())
			number_of_words = len(full_text.split())
			print(f"Number of words after preprocess: {number_of_words}")
			# wordcloud = WordCloud(background_color='white',
			#                       contour_width=3,
			#                       max_words=5000,
			#                       contour_color='steelblue',
			#                       width=1000,
			#                       height=1000).generate(full_text)
			# wordcloud.to_file(f"wordcloud_{RomanianParty.get_name(manifesto.metadata.party_id)}.png")
			manifesto_corpus.append(full_text)
			print(full_text)
	except Exception as e:
		print(f"Error occurred: {str(e)}")
		import traceback
		print(f"Full traceback: {traceback.format_exc()}")

	tfidf = TfidfVectorizer()
	tfidf_matrix = tfidf.fit_transform(manifesto_corpus)
	feature_names = tfidf.get_feature_names_out()  # mersi geeksforgeeks aparent e outdated tutorialu vostru

	# 2.098 = apare doar in unul din documente
	# 1.693 = apare doar in 2 documente
	# 1.405 = apare in 3 documente
	# 1.182 = apare in 4 documente
	# 1 = apare in toate

	# afisam toate idf values
	# print('\nIDF values:')
	# for feature_name, idf_value in zip(feature_names, tfidf.idf_):
	# 	print(f'{feature_name} : {idf_value}')

	analyze_word_commonality(feature_names, tfidf.idf_, len(manifesto_data), top_n=10000, reversed_order=False)

	similarity_matrix = cosine_similarity(tfidf_matrix)
	party_names = [RomanianParty.get_name(manifesto.metadata.party_id) for manifesto in manifesto_data]
	similarity_df = pd.DataFrame(similarity_matrix, columns=party_names, index=party_names)

	# Matricea de similiaritate intre documente cu TF-IDF
	pd.set_option('display.max_columns', None)
	pd.set_option('display.width', None)
	similarity_df = pd.DataFrame(similarity_matrix, columns=party_names, index=party_names)
	print("\nFull Document Similarity Matrix with TF-IDF:")
	print(similarity_df)

	# Matricea de similiaritate intre manifesto-uri cu codurile de la Manifesto Project
	print("\nFull Document Similarity Matrix with Hand Coding frequencies:")
	code_similarity_df = calculate_hand_coded_similarity(manifesto_data, party_names)
	print(code_similarity_df)

	# Cuvintele distinctive pentru fiecare partid
	print("\nAnalyzing distinctive vocabulary for each party:")
	find_party_specific_vocabulary(tfidf_matrix, feature_names, party_names)

	# Top coduri si procentajele pentru fiecare partid
	analyze_party_codes(manifesto_data)

	# Initialize and use
	topic_modeler = ManifestoTopicModeling()
	model, party_topics, topic_df = topic_modeler.perform_topic_modeling(
		manifesto_corpus,
		party_names
	)

	# Print the detailed topic DataFrame
	print("\nDetailed Topic Analysis:")
	pd.set_option('display.max_colwidth', None)
	print(topic_df)

	# Usage
	print_sentiment_analysis(manifesto_data, party_names, party_topics, model)

	while True:
		search_word = input("\nEnter a word to search for (or 'quit' to exit): ")
        # cuvinte interesante: pension, justice, corruption, education, health,
		if search_word.lower() == 'quit':
			break

		find_word_in_manifestos(search_word, manifesto_data, manifesto_corpus)

if __name__ == "__main__":
	main()
