from dataclasses import dataclass
from typing import Optional, Dict, Any, List


@dataclass
class ManifestoMetadata:
	manifesto_id: str
	party_id: int
	election_date: str
	language: str
	source: str
	has_eu_code: bool
	is_primary_doc: bool
	may_contradict_core_dataset: bool
	md5sum_text: Optional[str]
	url_original: Optional[str]
	md5sum_original: Optional[str]
	annotations: bool
	handbook: str
	is_copy_of: Optional[str]
	title: str
	translation_en: bool

	@classmethod
	def from_api_response(cls, data: Dict[str, Any]) -> 'ManifestoMetadata':
		"""
		Creeaza instanta de metadata a manifestului din datele primite de la API
		"""
		return cls(
			manifesto_id=str(data.get('manifesto_id', '')),
			party_id=int(data.get('party_id', 0)),
			election_date=str(data.get('election_date', '')),
			language=str(data.get('language', '')),
			source=str(data.get('source', '')),
			has_eu_code=bool(data.get('has_eu_code', False)),
			is_primary_doc=bool(data.get('is_primary_doc', False)),
			may_contradict_core_dataset=bool(data.get('may_contradict_core_dataset', False)),
			md5sum_text=data.get('md5sum_text'),
			url_original=data.get('url_original'),
			md5sum_original=data.get('md5sum_original'),
			annotations=bool(data.get('annotations', False)),
			handbook=str(data.get('handbook', '')),
			is_copy_of=data.get('is_copy_of'),
			title=str(data.get('title', '')),
			translation_en=bool(data.get('translation_en', False))
		)


@dataclass
class ManifestoTextItem:
	"""
	Un Text hand coded din manifesto
	"""
	text: str
	cmp_code: str   # Classification code from the Manifesto Project
	eu_code: str    # EU-specific care de la 2016 specific nu mai e folosit pt romania,
					# e folosit pt tari care tranzitionreaza spre democratie/ue

	@classmethod
	def from_api_response(cls, data: Dict[str, Any]) -> 'ManifestoTextItem':
		"""Cream o instanta din datele de la api"""
		return cls(
			text=str(data.get('text', '')),
			cmp_code=str(data.get('cmp_code', '')),
			eu_code=str(data.get('eu_code', 'NA'))
		)


@dataclass
class ManifestoContent:
	"""
	Reprezinta metadata+text_items
	"""
	metadata: ManifestoMetadata
	text_items: List[ManifestoTextItem]

	def get_full_text(self) -> str:
		"""Returneaza tot textul manifest-ului concatenat"""
		return ' '.join(item.text for item in self.text_items)

	def get_items_by_code(self, cmp_code: str) -> List[ManifestoTextItem]:
		"""Returneaza toate itemele cu un anumit cmp_code"""
		return [item for item in self.text_items if item.cmp_code == cmp_code]