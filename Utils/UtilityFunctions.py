import spacy
import re

from nltk.corpus import stopwords

from Utils.Enums import RomanianParty


def preprocess_text(text):
	nlp = spacy.load('en_core_web_sm')
	text = text.lower()
	text = re.sub(r'[^\w\s-]', ' ', text)
	doc = nlp(text)
	# get stopwords
	# nltk.download('stopwords') asta trb rulat doar o data
	stop_words = set(stopwords.words('english'))

	# fara stopwords, tinem doar substantive, adjective si verbe, lematizam cuvintele, le scoatem si pe alea scurte
	meaningful_words = [token.lemma_ for token in doc
	                    if (token.pos_ in ['NOUN', 'ADJ', 'VERB'] and
	                        not token.is_stop and
	                        len(token.text) > 2)]

	return ' '.join(meaningful_words)


def find_word_in_manifestos(word, manifesto_data, manifesto_corpus):
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(word.lower())

	if len(doc) > 0:
		search_word = doc[0].lemma_
	else:
		print("Please enter a valid word")
		return

	print(f"\nSearching for the lemmatized word '{search_word}' in all manifestos:")

	found_anywhere = False

	for i in range(len(manifesto_data)):
		current_manifesto = manifesto_data[i]
		preprocessed_text = manifesto_corpus[i]

		words_in_text = preprocessed_text.split()

		word_count = 0
		for text_word in words_in_text:
			if text_word == search_word:
				word_count = word_count + 1

		if word_count > 0:
			party_name = RomanianParty.get_name(current_manifesto.metadata.party_id)
			print(f"Found in {party_name}'s manifesto ({word_count} times)")
			found_anywhere = True

	if not found_anywhere:
		print(f"The word '{search_word}' was not found in any manifesto.")
		print("Note: Words are lemmatized and only nouns, adjectives, and verbs are kept.")
		print("Try searching for the base form of the word (e.g., 'vote' instead of 'voting')")
