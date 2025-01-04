
from typing import Any, List, Optional, Dict

import requests

from api.Models import ManifestoMetadata, ManifestoContent, ManifestoTextItem


class ManifestoAPI:
	def __init__(self, api_key: str):
		self.base_url = "https://manifesto-project.wzb.eu/api/v1"
		self.api_key = api_key

	def _make_request(self, endpoint: str, params: Dict[str, Any], expect_json: bool = True) -> Any:
		try:
			response = requests.get(
				f"{self.base_url}/{endpoint}",
				params=params,
				timeout=30
			)
			response.raise_for_status()

			if expect_json:
				return response.json()
			return response.content

		except requests.exceptions.RequestException as e:
			raise requests.exceptions.RequestException(
				f"API request failed: {str(e)}\n"
				f"Endpoint: {endpoint}\n"
				f"Params: {params}"
			)

	def get_core_versions(self) -> Dict:
		params = {"api_key": self.api_key}
		return self._make_request("list_core_versions", params, expect_json=True)

	def get_core(self, key: str, kind: str = "xlsx", raw: bool = False) -> bytes:
		params = {
			"api_key": self.api_key,
			"key": key,
			"kind": kind,
			"raw": str(raw).lower()
		}
		return self._make_request("get_core", params, expect_json=False)

	def get_metadata(self, keys: List[str], version: str) -> Dict:
		params = {
			"api_key": self.api_key,
			"version": version,
			**{"keys[]": key for key in keys}
		}
		return self._make_request("metadata", params, expect_json=True)

	def get_texts_and_annotations(
			self,
			keys: List[str],
			version: str,
			translation: Optional[str] = None
	) -> Dict:
		params = {
			"api_key": self.api_key,
			"version": version,
			**{"keys[]": key for key in keys}
		}
		if translation:
			params["translation"] = translation
		return self._make_request("texts_and_annotations", params, expect_json=True)

	def get_manifesto_content(
			self,
			manifesto_id: str,
			version: str = "2024-1",
			translation: Optional[str] = "en"
	) -> Optional[ManifestoContent]:
		# Luam mai intai metadata
		metadata_response = self.get_metadata([manifesto_id], version)
		if not metadata_response.get('items'):
			return None

		metadata = ManifestoMetadata.from_api_response(metadata_response['items'][0])

		# Apoi luam content-ul daca are
		text_items: List[ManifestoTextItem] = []
		if metadata.annotations:
			text_response = self.get_texts_and_annotations(
				keys=[manifesto_id],
				version=version,
				translation=translation
			)

			if text_response.get('items'):
				# Extract text items from the response
				for item in text_response['items'][0].get('items', []):
					text_items.append(ManifestoTextItem.from_api_response(item))

		return ManifestoContent(metadata=metadata, text_items=text_items)

	def fetch_manifestos(
			self,
			manifesto_ids: List[str],
			version: str = "2024-1",
			translation: Optional[str] = "en"
	) -> List[ManifestoContent]:

		print(f"Fetching {len(manifesto_ids)} manifestos...")
		results: List[ManifestoContent] = []

		for manifesto_id in manifesto_ids:
			try:
				content = self.get_manifesto_content(
					manifesto_id=manifesto_id,
					version=version,
					translation=translation
				)
				if content:
					results.append(content)
					print(f"Successfully fetched manifesto: {manifesto_id}")
			except Exception as e:
				print(f"Failed to fetch manifesto {manifesto_id}: {str(e)}")

		return results


def fetch_manifesto_metadata(api: ManifestoAPI, manifesto_ids: List[str], version: str = "2024-1") -> Dict:
	try:
		print(f"\nSe obține metadata pentru {len(manifesto_ids)} manifeste...")
		metadata = api.get_metadata(manifesto_ids, version=version)

		available_texts = []
		processed_results = []

		for item in metadata.get('items', []):
			manifesto_id = item.get('manifesto_id')
			manifest_info = {
				'manifesto_id': manifesto_id,
				'title': item.get('title', 'N/A'),
				'date': item.get('date', 'N/A'),
				'party': item.get('party', 'N/A'),
				'language': item.get('language', 'N/A'),
				'has_text': item.get('annotations', False)
			}
			processed_results.append(manifest_info)

			if item.get('annotations', False):
				available_texts.append(manifesto_id)
				print(f"Text disponibil pentru manifestul: {manifesto_id}")

		return {
			'processed_metadata': processed_results,
			'available_texts': available_texts
		}

	except Exception as e:
		print(f"Eroare la obținerea metadata: {str(e)}")
		raise