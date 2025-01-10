from enum import Enum

class ManifestoCodes(Enum):
	# Domain 1: External Relations (101-110)
	FOREIGN_RELATIONS_POS = ('per101', 'Foreign Special Relationships: Positive')
	FOREIGN_RELATIONS_NEG = ('per102', 'Foreign Special Relationships: Negative')
	ANTI_IMPERIALISM = ('per103', 'Anti-Imperialism')
	MILITARY_POS = ('per104', 'Military: Positive')
	MILITARY_NEG = ('per105', 'Military: Negative')
	PEACE = ('per106', 'Peace')
	INTERNATIONALISM_POS = ('per107', 'Internationalism: Positive')
	EU_POS = ('per108', 'European Community/Union: Positive')
	INTERNATIONALISM_NEG = ('per109', 'Internationalism: Negative')
	EU_NEG = ('per110', 'European Community/Union: Negative')

	# Domain 2: Freedom and Democracy (201-204)
	FREEDOM = ('per201', 'Freedom and Human Rights')
	DEMOCRACY = ('per202', 'Democracy')
	CONSTITUTIONALISM_POS = ('per203', 'Constitutionalism: Positive')
	CONSTITUTIONALISM_NEG = ('per204', 'Constitutionalism: Negative')

	# Domain 3: Political System (301-305)
	DECENTRALIZATION = ('per301', 'Decentralization')
	CENTRALIZATION = ('per302', 'Centralization')
	EFFICIENCY = ('per303', 'Governmental and Administrative Efficiency')
	CORRUPTION = ('per304', 'Political Corruption')
	AUTHORITY = ('per305', 'Political Authority')

	# Domain 4: Economy (401-416)
	FREE_MARKET = ('per401', 'Free Market Economy')
	INCENTIVES = ('per402', 'Incentives: Positive')
	MARKET_REGULATION = ('per403', 'Market Regulation')
	ECONOMIC_PLANNING = ('per404', 'Economic Planning')
	CORPORATISM = ('per405', 'Corporatism/Mixed Economy')
	PROTECTIONISM_POS = ('per406', 'Protectionism: Positive')
	PROTECTIONISM_NEG = ('per407', 'Protectionism: Negative')
	ECONOMIC_GOALS = ('per408', 'Economic Goals')
	KEYNESIAN = ('per409', 'Keynesian Demand Management')
	GROWTH = ('per410', 'Economic Growth: Positive')
	TECHNOLOGY = ('per411', 'Technology and Infrastructure: Positive')
	CONTROLLED_ECONOMY = ('per412', 'Controlled Economy')
	NATIONALIZATION = ('per413', 'Nationalization')
	ECONOMIC_ORTHODOXY = ('per414', 'Economic Orthodoxy')
	MARXIST = ('per415', 'Marxist Analysis')
	ANTI_GROWTH = ('per416', 'Anti-Growth Economy: Positive')

	# Domain 5: Welfare and Quality of Life (501-507)
	ENVIRONMENT = ('per501', 'Environmental Protection')
	CULTURE = ('per502', 'Culture: Positive')
	EQUALITY = ('per503', 'Equality: Positive')
	WELFARE_EXPANSION = ('per504', 'Welfare State Expansion')
	WELFARE_LIMITATION = ('per505', 'Welfare State Limitation')
	EDUCATION_EXPANSION = ('per506', 'Education Expansion')
	EDUCATION_LIMITATION = ('per507', 'Education Limitation')

	# Domain 6: Fabric of Society (601-608)
	NATIONAL_WAY_POS = ('per601', 'National Way of Life: Positive')
	NATIONAL_WAY_NEG = ('per602', 'National Way of Life: Negative')
	MORALITY_POS = ('per603', 'Traditional Morality: Positive')
	MORALITY_NEG = ('per604', 'Traditional Morality: Negative')
	LAW_AND_ORDER = ('per605', 'Law and Order: Positive')
	CIVIC_MINDEDNESS = ('per606', 'Civic Mindedness: Positive')
	MULTICULTURALISM_POS = ('per607', 'Multiculturalism: Positive')
	MULTICULTURALISM_NEG = ('per608', 'Multiculturalism: Negative')

	# Domain 7: Social Groups (701-706)
	LABOR_POS = ('per701', 'Labour Groups: Positive')
	LABOR_NEG = ('per702', 'Labour Groups: Negative')
	AGRICULTURE = ('per703', 'Agriculture and Farmers: Positive')
	MIDDLE_CLASS = ('per704', 'Middle Class and Professional Groups')
	MINORITY_GROUPS = ('per705', 'Underprivileged Minority Groups')
	DEMOGRAPHIC_GROUPS = ('per706', 'Non-economic Demographic Groups')

	# Subcategories (Type 2)
	# Anti-Imperialism subcategories
	ANTI_IMPERIALISM_STATE = ('per103_1', 'Anti-Imperialism: State Centred')
	ANTI_IMPERIALISM_FINANCIAL = ('per103_2', 'Anti-Imperialism: Foreign Financial Influence')

	# Freedom and Human Rights subcategories
	FREEDOM_PERSONAL = ('per201_1', 'Freedom: Personal Freedom and State Control')
	FREEDOM_HUMAN_RIGHTS = ('per201_2', 'Freedom: Human and Civil Rights')

	# Democracy subcategories
	DEMOCRACY_GENERAL_POS = ('per202_1', 'Democracy General: Positive')
	DEMOCRACY_GENERAL_NEG = ('per202_2', 'Democracy General: Negative')
	DEMOCRACY_REPRESENTATIVE = ('per202_3', 'Representative Democracy: Positive')
	DEMOCRACY_DIRECT = ('per202_4', 'Direct Democracy: Positive')

	# Political Authority subcategories
	AUTHORITY_PARTY = ('per305_1', 'Political Authority: Party Competence')
	AUTHORITY_PERSONAL = ('per305_2', 'Political Authority: Personal Competence')
	AUTHORITY_STRONG = ('per305_3', 'Political Authority: Strong Government')
	AUTHORITY_TRANSITION_POS = ('per305_4', 'Transition: Pre-Democratic Elites: Positive')
	AUTHORITY_TRANSITION_NEG = ('per305_5', 'Transition: Pre-Democratic Elites: Negative')
	AUTHORITY_REHABILITATION = ('per305_6', 'Transition: Rehabilitation and Compensation')

	# Anti-Growth subcategories
	ANTI_GROWTH_GENERAL = ('per416_1', 'Anti-Growth Economy: General')
	ANTI_GROWTH_SUSTAINABILITY = ('per416_2', 'Anti-Growth Economy: Sustainability')

	# National Way of Life subcategories
	NATIONAL_WAY_GENERAL_POS = ('per601_1', 'National Way of Life General: Positive')
	NATIONAL_WAY_IMMIGRATION_NEG = ('per601_2', 'National Way of Life: Immigration: Negative')
	NATIONAL_WAY_GENERAL_NEG = ('per602_1', 'National Way of Life General: Negative')
	NATIONAL_WAY_IMMIGRATION_POS = ('per602_2', 'National Way of Life: Immigration: Positive')

	# Law and Order subcategories
	LAW_ORDER_POS = ('per605_1', 'Law and Order: Enforcement: Positive')
	LAW_ORDER_NEG = ('per605_2', 'Law and Order: Enforcement: Negative')

	# Civic Mindedness subcategories
	CIVIC_GENERAL = ('per606_1', 'Civic Mindedness General: Positive')
	CIVIC_BOTTOM_UP = ('per606_2', 'Civic Mindedness: Bottom-Up Activism')

	# Multiculturalism subcategories
	MULTICULT_GENERAL_POS = ('per607_1', 'Multiculturalism General: Positive')
	MULTICULT_IMMIGRANTS_POS = ('per607_2', 'Multiculturalism: Immigrants Diversity')
	MULTICULT_INDIGENOUS_POS = ('per607_3', 'Multiculturalism: Indigenous Rights: Positive')
	MULTICULT_GENERAL_NEG = ('per608_1', 'Multiculturalism General: Negative')
	MULTICULT_IMMIGRANTS_NEG = ('per608_2', 'Multiculturalism: Immigrants Assimilation')
	MULTICULT_INDIGENOUS_NEG = ('per608_3', 'Multiculturalism: Indigenous Rights: Negative')

	# Agriculture subcategories
	AGRICULTURE_POS = ('per703_1', 'Agriculture and Farmers: Positive')
	AGRICULTURE_NEG = ('per703_2', 'Agriculture and Farmers: Negative')

	@classmethod
	def get_description(cls, code):
		if code == 'H':
			return 'Headers/Titles'
		if code == 'NA':
			return 'Not Applicable'

		if '.' in code:
			code_to_check = 'per' + code.replace('.', '_')
		else:
			code_to_check = 'per' + code if not code.startswith('per') else code

		for member in cls:
			if member.value[0] == code_to_check:
				return member.value[1]
		return "Unknown Code"


class RomanianParty(Enum):
	PSD = 93223
	PNL = 93430
	USR = 93440
	PMP = 93540
	UDMR = 93951

	@classmethod
	def get_name(cls, party_id: int) -> str:
		try:
			return cls(party_id).name
		except ValueError:
			return f"Unknown Party ({party_id})"

class TopicTheme(Enum):
    HEALTHCARE = 0              # health, hospital, patient
    PUBLIC_ADMINISTRATION = 1           # public administration, service
    YOUTH_EDUCATION = 3        # young, people, sport, education
    ENERGY_ENVIRONMENT = 4     # energy, forest, electricity
    ECONOMY_FINANCE = 5        # tax, income, gdp
    INFRASTRUCTURE = 6         # port, infrastructure, transport
    EDUCATION_REFORM = 7       # education, teacher, student
    CULTURE_IDENTITY = 8       # cultural, culture, artist
    INTERNATIONAL_RELATIONS = 9         # partnership, strategic, security
    REGIONAL_COMMUNITY = 10    # transylvania, community, family

    @classmethod
    def get_name(cls, topic_id: int) -> str:
        try:
            return cls(topic_id).name.replace('_', ' ').title()
        except ValueError:
            return f"Topic {topic_id}"