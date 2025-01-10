from gensim.models import LdaModel, Phrases
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
import spacy
import numpy as np
from typing import List, Tuple, Dict
import logging
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

from Utils.Enums import TopicTheme


class ManifestoTopicModeling:
	def __init__(self):
		# Parametri umap pentru reducerea dimensionalitatii
		self.umap_model = UMAP(
			n_neighbors=5,
			n_components=5,  # Nr la care reducem
			min_dist=0.0,  # In context politic asta pare sa aiba sens
			metric='cosine',
			random_state=42
		)


		# Parametri pt clustering
		self.hdbscan_model = HDBSCAN(
			min_cluster_size=2,
			metric='euclidean',
			cluster_selection_method='eom',
			prediction_data=True
		)


		# Controlam ce cuivnte folosim
		self.vectorizer_model = CountVectorizer(
			stop_words='english',
			min_df=2,
			max_df=0.95
		)

		# Parametri BERT
		self.topic_model = BERTopic(
			embedding_model="all-MiniLM-L6-v2",
			umap_model=self.umap_model,
			hdbscan_model=self.hdbscan_model,
			vectorizer_model=self.vectorizer_model,
			verbose=True
		)

	def chunk_document(self, text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:

		# Split in chunk-uri cu un pic de overlap
		words = text.split()
		chunks = []

		# procesam document-ul pe chunk-uri
		current_position = 0
		while current_position < len(words):

			end_position = current_position + chunk_size
			current_chunk = words[current_position:end_position]

			# macar jumatate din chunk
			if len(current_chunk) >= chunk_size // 2:
				chunk_text = ' '.join(current_chunk)
				chunks.append(chunk_text)

			current_position = current_position + (chunk_size - overlap)

		return chunks

	def perform_topic_modeling(self, manifesto_corpus: List[str], party_names: List[str]) -> Tuple[
		BERTopic, Dict[str, List[int]], pd.DataFrame]:

		all_chunks = []
		chunk_labels = []

		# Procesam fiecare manifesto
		for i in range(len(manifesto_corpus)):
			text = manifesto_corpus[i]
			party_name = party_names[i]

			# Split in chunk-uri
			document_chunks = self.chunk_document(text)

			# Adaugam chunk-urile si party name urile corespunzatoare
			for chunk in document_chunks:
				all_chunks.append(chunk)
				chunk_labels.append(party_name)

		topics, probs = self.topic_model.fit_transform(all_chunks)

		topic_info = self.topic_model.get_topic_info()

		# Analizam distributia pt fiecare partid
		party_topics = {}
		for party in party_names:

			party_indices = []
			for i in range(len(chunk_labels)):
				if chunk_labels[i] == party:
					party_indices.append(i)

			if party_indices:
				party_topics_list = []
				for i in party_indices:
					topic = topics[i]
					if topic != -1:  # le ignoram pe alea outliers
						party_topics_list.append(topic)

				# Numaram de ficare data cand apare un topic
				if party_topics_list:
					topic_counts = np.bincount(party_topics_list)

					# Le luam pe cele mai populare 3
					dominant_topics = []
					sorted_indices = np.argsort(topic_counts)

					for i in reversed(sorted_indices[-3:]):
						dominant_topics.append(i)

					party_topics[party] = dominant_topics

		# Cream o reprezentare mai frumoasa
		topic_representations = []
		for party in party_topics:
			top_topics = party_topics[party]
			for topic_index in top_topics:
				if topic_index != -1:  # skip outlier

					topic_words = []
					topic_word_data = self.topic_model.get_topic(topic_index)
					for word_data in topic_word_data[:10]:
						topic_words.append(word_data[0])  # word_data e (word, score)

					topic_size = 0
					for i, row in topic_info.iterrows():
						if row['Topic'] == topic_index:
							topic_size = row['Count']
							break

					topic_data = {
						'Party': party,
						'Topic_ID': topic_index,
						'Top_Words': ', '.join(topic_words),
						'Size': topic_size
					}
					topic_representations.append(topic_data)

		topic_df = pd.DataFrame(topic_representations)

		print("\nTopic Modeling Results:")
		print(f"Total number of topics found: {len(topic_info[topic_info['Topic'] != -1])}")
		print("\nTop topics per party:")

		# Prin topic-uri pt fiecare party
		for party in party_topics:
			print(f"\n{party}:")
			top_topics = party_topics[party]
			for topic_index in top_topics:
				if topic_index != -1:
					topic_words = []
					topic_word_data = self.topic_model.get_topic(topic_index)
					for word_data in topic_word_data[:5]:
						topic_words.append(word_data[0])
					print(f"Topic: {TopicTheme.get_name(topic_index)}: {', '.join(topic_words)}")

		return self.topic_model, party_topics, topic_df