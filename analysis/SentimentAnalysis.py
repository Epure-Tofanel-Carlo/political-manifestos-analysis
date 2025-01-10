from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from typing import Dict, List, Tuple, Any
from nltk.corpus import wordnet

from Utils.UtilityFunctions import get_topic_sentences

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from nltk.corpus import wordnet
from typing import Dict, List, Tuple


class PoliticalSentimentAnalyzer:
	def __init__(self):
		self.analyzer = SentimentIntensityAnalyzer()
		self.update_lexicon()

	def update_lexicon(self):
		political_words = {
			'reform': 2.0,
			'corruption': 3.0,
			'bureaucracy': 2.0,
			'investment': 2.0,
			'modernization': 2.0,
			'progress': 1.8,
			'development': 1.5,
			'infrastructure': 1.5,
			'innovation': 1.8,
			'education': 1.5,
			'healthcare': 1.5,
			'transparency': 2.0,
			'unemployment': 1.8,
			'poverty': 2.0,
			'deficit': -1.5,
			'debt': -1.5,
			'growth': 1.8
		}
		self.analyzer.lexicon.update(political_words)

	def get_synonyms(self, word: str) -> List[str]:
		synonyms = set()
		for syn in wordnet.synsets(word):
			for lemma in syn.lemmas():
				synonyms.add(lemma.name())
		return list(synonyms)

	def preprocess_text(self, text: str) -> str:
		for punct in [';', '•', '!', '?']:
			text = text.replace(punct, '.')
		text = text.replace('n\'t', ' not')
		text = ' '.join(text.split())  # handle la spatii multiple
		text = text.replace('gdp', 'gross domestic product')
		text = text.replace('cass', 'health insurance')
		return text

	def analyze_party_topic_sentiment(self, manifesto: str, party: str, topic_words: List[str]) -> Dict:
		manifesto = self.preprocess_text(manifesto)
		synonyms = {}
		for word in topic_words:
			synonyms[word] = self.get_synonyms(word)

		sentences = []
		sentiment_results = []

		for sentence in manifesto.split('.'):
			sentence = sentence.strip()
			if not sentence:
				continue

			found_topic = False
			for word in topic_words:
				if word in sentence.lower() or any(syn in sentence.lower() for syn in synonyms[word]):
					found_topic = True
					break

			if found_topic:
				sentences.append(sentence)
				scores = self.analyzer.polarity_scores(sentence)
				sentiment_results.append({
					'party': party,
					'sentence': sentence,
					'compound': scores['compound'],
					'pos': scores['pos'],
					'neg': scores['neg'],
					'neu': scores['neu']
				})

		if not sentiment_results:
			return self.create_empty_analysis(party, topic_words)

		num_sentences = len(sentiment_results)
		avg_compound = 0
		avg_pos = 0
		avg_neg = 0
		avg_neu = 0

		for result in sentiment_results:
			avg_compound += result['compound']
			avg_pos += result['pos']
			avg_neg += result['neg']
			avg_neu += result['neu']

		return {
			'party': party,
			'topic_words': topic_words,
			'num_sentences': num_sentences,
			'avg_compound': avg_compound / num_sentences,
			'avg_positive': avg_pos / num_sentences,
			'avg_negative': avg_neg / num_sentences,
			'avg_neutral': avg_neu / num_sentences,
			'sentences': sentiment_results
		}

	def create_empty_analysis(self, party: str, topic_words: List[str]) -> Dict:
		return {
			'party': party,
			'topic_words': topic_words,
			'num_sentences': 0,
			'avg_compound': 0.0,
			'avg_positive': 0.0,
			'avg_negative': 0.0,
			'avg_neutral': 0.0,
			'sentences': []
		}

	def analyze_all_parties(self, manifestos: Dict[str, str], party_topics: Dict[str, List[List[str]]]) -> Tuple[
		pd.DataFrame, pd.DataFrame]:
		all_analyses = []

		for party, manifesto in manifestos.items():
			if party not in party_topics:
				continue

			for topic_words in party_topics[party]:
				analysis = self.analyze_party_topic_sentiment(manifesto, party, topic_words)
				all_analyses.append(analysis)

		if not all_analyses:
			return pd.DataFrame(), pd.DataFrame()

		results_rows = []
		sentence_rows = []

		for analysis in all_analyses:
			results_rows.append({
				'Party': analysis['party'],
				'Topic_Words': ', '.join(analysis['topic_words']),
				'Num_Sentences': analysis['num_sentences'],
				'Avg_Compound': analysis['avg_compound'],
				'Avg_Positive': analysis['avg_positive'],
				'Avg_Negative': analysis['avg_negative'],
				'Avg_Neutral': analysis['avg_neutral']
			})

			for sent in analysis['sentences']:
				sentence_rows.append({
					'Party': analysis['party'],
					'Topic_Words': ', '.join(analysis['topic_words']),
					'Sentence': sent['sentence'],
					'Compound': sent['compound'],
					'Positive': sent['pos'],
					'Negative': sent['neg'],
					'Neutral': sent['neu']
				})

		return pd.DataFrame(results_rows), pd.DataFrame(sentence_rows)


def print_sentiment_analysis(manifesto_data, party_names, party_topics, model):
	sentiment_analyzer = PoliticalSentimentAnalyzer()

	# manifesto_texts dictionary
	manifesto_texts = {}
	for i, manifesto in enumerate(manifesto_data):
		text = ''
		for item in manifesto.text_items:
			text += item.text + ' '
		manifesto_texts[party_names[i]] = text.strip()
		print(f"Processed {party_names[i]} manifesto - {len(text)} characters")

	# topic words dictionary
	party_topics_words = {}
	for party, topics_list in party_topics.items():
		topic_words = []
		for topic_id in topics_list:
			words = []
			for word, _ in model.get_topic(topic_id)[:10]:
				words.append(word)
			topic_words.append(words)
			print(f"{party} Topic {topic_id}: {', '.join(words)}")
		party_topics_words[party] = topic_words

	results_df, sentence_df = sentiment_analyzer.analyze_all_parties(
		manifesto_texts,
		party_topics_words
	)

	if results_df.empty:
		print("No sentiment analysis results generated")
		return

	print("\nSentiment Analysis Summary:")
	pd.set_option('display.max_columns', None)
	pd.set_option('display.float_format', '{:.3f}'.format)
	print(results_df)

	# Sample propoziiti
	print("\nMost Significant Sentences by Party:")
	for party in party_names:
		party_data = sentence_df[sentence_df['Party'] == party]
		if not party_data.empty:
			print(f"\n{party}:")

			# Cele mai negative
			most_neg = party_data.loc[party_data['Compound'].idxmin()]
			print("Most Negative:")
			print(f"Topic: {most_neg['Topic_Words'][:300]}...")
			print(f"Sentence: {most_neg['Sentence']}")
			print(
				f"Scores: Compound={most_neg['Compound']:.3f}, Pos={most_neg['Positive']:.3f}, Neg={most_neg['Negative']:.3f}")
			print()

			# Cele mai pozitive
			most_pos = party_data.loc[party_data['Compound'].idxmax()]
			print("Most Positive:")
			print(f"Topic: {most_pos['Topic_Words'][:300]}...")
			print(f"Sentence: {most_pos['Sentence']}")
			print(
				f"Scores: Compound={most_pos['Compound']:.3f}, Pos={most_pos['Positive']:.3f}, Neg={most_pos['Negative']:.3f}")
			print()

			# Cel mai aproape de compound 0
			most_neu = party_data.loc[(party_data['Compound']).abs().idxmin()]
			print("Most Neutral:")
			print(f"Topic: {most_neu['Topic_Words'][:300]}...")
			print(f"Sentence: {most_neu['Sentence']}")
			print(
				f"Scores: Compound={most_neu['Compound']:.3f}, Pos={most_neu['Positive']:.3f}, Neg={most_neu['Negative']:.3f}")
			print()


