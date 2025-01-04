import numpy as np
import pandas as pd

from Utils.Enums import RomanianParty, ManifestoCodes


def calculate_hand_coded_similarity(manifesto_data, party_names):
	code_vectors = []

	for manifesto in manifesto_data:
		# de cate ori apare fiecare cod
		code_counts = {}
		for item in manifesto.text_items:
			code_counts[item.cmp_code] = code_counts.get(item.cmp_code, 0) + 1

		# le facem frecvente ca sa nu fie influentate de numarul total de coduri (udmr e mai scurt)
		total_codes = sum(code_counts.values())
		code_frequencies = {code: count / total_codes
		                    for code, count in code_counts.items()}

		code_vectors.append(code_frequencies)

	# cosine similarity intre codurile partidelor
	code_similarity = np.zeros((len(party_names), len(party_names)))
	for i in range(len(party_names)):
		for j in range(len(party_names)):
			similarity = 0
			# toate codurile unice de la almbele partide
			all_codes = set(code_vectors[i].keys()) | set(code_vectors[j].keys())

			# dot product
			numerator = sum(code_vectors[i].get(code, 0) * code_vectors[j].get(code, 0)
			                for code in all_codes)
			# magnitudinea vectorilor
			mag_i = float(sum(v * v for v in code_vectors[i].values())) ** 0.5
			mag_j = float(sum(v * v for v in code_vectors[j].values())) ** 0.5

			if mag_i and mag_j:  # sa nu avem division by zero
				similarity = numerator / (mag_i * mag_j)
				code_similarity[i, j] = similarity

	# facem un dataframe
	code_similarity_df = pd.DataFrame(code_similarity,
	                                  index=party_names,
	                                  columns=party_names)

	return code_similarity_df


def analyze_party_codes(manifesto_data, top_n=10):
	print("\nTop hand codes for each party:")

	for manifesto in manifesto_data:
		# numaram de fiecare data cand apare un cod
		code_counts = {}
		for item in manifesto.text_items:
			if item.cmp_code == 'H':
				continue
			code_counts[item.cmp_code] = code_counts.get(item.cmp_code, 0) + 1

		# le convertim in lista de tupluri
		code_list = []
		for code, count in code_counts.items():
			code_list.append((code, count))

		# luam al doilea item
		def get_count(item):
			return item[1]

		# sortam dupa al doilea item
		sorted_codes = sorted(code_list, key=get_count, reverse=True)

		# luam primele n coduri
		top_codes = []
		for i in range(min(top_n, len(sorted_codes))):
			top_codes.append(sorted_codes[i])

		party_name = RomanianParty.get_name(manifesto.metadata.party_id)
		print(f"\n{party_name}:")

		for code, count in top_codes:
			# calculam procentajele
			total_items = len(manifesto.text_items)
			percentage = (count / total_items) * 100
			description = ManifestoCodes.get_description(code)

			print(f"Code {code} - {description}: {count} times ({percentage:.1f}%)")
