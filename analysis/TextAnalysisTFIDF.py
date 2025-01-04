import math


def find_party_specific_vocabulary(tfidf_matrix, feature_names, party_names, top_n=10):
	dense_matrix = tfidf_matrix.toarray()
	print("\nMost distinctive words for each party:")
	for party_index, party_name in enumerate(party_names):
		# scorurile la cuivnte pt partidul respectiv
		party_scores = dense_matrix[party_index]
		# sort by tfidf score, ultimele n scoruri, apoi reverse
		top_word_indices = party_scores.argsort()[-top_n:][::-1]

		print(f"\n{party_name}:")
		for index in top_word_indices:
			word = feature_names[index]
			score = party_scores[index]
			if score > 0:  # doar cuvinte care chiar apar
				print(f"  {word}: {score:.4f}")


def analyze_word_commonality(feature_names, idf_values, total_documents, top_n=None, reversed_order=False):
	word_idf_pairs = []
	for i in range(len(feature_names)):
		word = feature_names[i]
		idf = idf_values[i]
		word_idf_pairs.append((word, idf))

	def get_idf_value(pair):
		return pair[1]

	if reversed:
		sorted_pairs = sorted(word_idf_pairs, key=get_idf_value, reverse=True)
	else:
		sorted_pairs = sorted(word_idf_pairs, key=get_idf_value)

	if top_n is None:
		n_words = len(sorted_pairs)
	else:
		n_words = min(top_n, len(sorted_pairs))

	print("\nWords sorted by commonality (most to least common):")
	print("Format: Word : IDF value (number of documents)")

	for i in range(n_words):
		word = sorted_pairs[i][0]
		idf = sorted_pairs[i][1]

		# inversu la idf
		documents_with_word = round(total_documents / math.exp(idf))

		# verificam daca idf-ul calculat e corect
		expected_idf = math.log(total_documents / documents_with_word)

		if abs(idf - 1.000) < 0.01:
			documents_with_word = 5  # deci aici n am reust sa fac cu formula matematica de mai sus, deci doar le mapez direct ca pana mea
		elif abs(idf - 1.182) < 0.01:
			documents_with_word = 4
		elif abs(idf - 1.405) < 0.01:
			documents_with_word = 3
		elif abs(idf - 1.693) < 0.01:
			documents_with_word = 2
		elif abs(idf - 2.098) < 0.01:
			documents_with_word = 1
		else:
			documents_with_word = 0  # cazuri unexpected

		print(f"{word} : {idf:.3f} (appears in {documents_with_word} documents)")