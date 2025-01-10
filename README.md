# political-manifestos-analysis

## Example output:

# political-manifestos-analysis

## Example output:

```
Fetching 5 manifestos...
Successfully fetched manifesto: 93223_201612  
Successfully fetched manifesto: 93430_201612
Successfully fetched manifesto: 93440_201612
Successfully fetched manifesto: 93540_201612
Successfully fetched manifesto: 93951_201612
```

```
Manifesto Details:
Title: Programul de guvernare al Partidului Social Democrat. Proiectul bugetului general consolidat 2017
Party: PSD
Election Date: 201612
Language: romanian
Number of text items: 1171

All the text:
Number of words before preprocess: 9545
Number of words after preprocess: 5233
govern programme draft general consolidated budget romanian middle class face great opportunity lei transfer money pocket romanian main direction budget increase household income increase minimum wage increase wage education health public sector employee average wage growth increase pension point guarantee minimum pension increase...
```

```
Manifesto Details:
Title: 100 de măsuri liberale în completarea proiectelor prezentate de Dacian Cioloş prin Platforma România 100
Party: PNL
Election Date: 201612
Language: romanian
Number of text items: 224

All the text:
Number of words before preprocess: 3414
Number of words after preprocess: 1757
liberal measure addition project present dacian ciolo platform propose liberal measure addition project present dacian ciolo platform liberal measure national recovery fiscal budgetary policy generalization single rate social contribution aim tax relaxation simplification implement short term social contribution cas cass unemployment risk fund employee employer...
```

```
Manifesto Details:
Title: Uniunea Salvati România. Program Național
Party: USR
Election Date: 201612
Language: romanian
Number of text items: 575

All the text:
Number of words before preprocess: 9595
Number of words after preprocess: 4846
program transparency live democratic country rich natural resource talented work commit people poor compare neighbour possibility quality life low live poverty line poor housing condition manage community daily life difficult concrete car natural question ask way fight theft corruption year public money steal successive politician doesn matter right wing left wing pseudo independent politician rule serve party group interest...
```

```
Manifesto Details:
Title: O naţiune liberă, activă şi unită
Party: PMP
Election Date: 201612
Language: romanian
Number of text items: 410

All the text:
Number of words before preprocess: 5747
Number of words after preprocess: 2931
free active united nation suffer trust deficit today parallel neglect national value mockery patriotism rejection european identity stand increase social cohesion today severe threat inequality poverty combine rise unemployment young people extreme...
```

```
Manifesto Details:
Title: Transilvania, viitorul pentru noi toţi! Proiectele UDMR până în anul 2020
Party: UDMR
Election Date: 201612
Language: romanian
Number of text items: 82

All the text:
Number of words before preprocess: 1060
Number of words after preprocess: 461
future rmdsz project year present active romanian parliament government opposition objective obtain right local community security family support good coexistence romanian hungarian achievement proud result know perfect aware lot year propose series measure...
```

```
Full Document Similarity Matrix with TF-IDF:
           PSD       PNL       USR       PMP      UDMR
PSD   1.000000  0.501380  0.432734  0.338009  0.272371
PNL   0.501380  1.000000  0.587257  0.491669  0.289203
USR   0.432734  0.587257  1.000000  0.599377  0.303576
PMP   0.338009  0.491669  0.599377  1.000000  0.274496
UDMR  0.272371  0.289203  0.303576  0.274496  1.000000
```

```
Full Document Similarity Matrix with Hand Coding frequencies:
           PSD       PNL       USR       PMP      UDMR
PSD   1.000000  0.736741  0.750338  0.442850  0.675618
PNL   0.736741  1.000000  0.844460  0.609638  0.573852
USR   0.750338  0.844460  1.000000  0.731807  0.700277
PMP   0.442850  0.609638  0.731807  1.000000  0.526453
UDMR  0.675618  0.573852  0.700277  0.526453  1.000000
```

```
Analyzing distinctive vocabulary for each party:

Most distinctive words for each party:

PSD:
  lei: 0.4061
  programme: 0.2287
  year: 0.2141
  budget: 0.2043
  young: 0.1805
  increase: 0.1780
  people: 0.1702
  tax: 0.1651
  gdp: 0.1377
  fund: 0.1372

PNL:
  fund: 0.2002
  tax: 0.1787
  investment: 0.1557
  national: 0.1557
  increase: 0.1505
  service: 0.1446
  school: 0.1317
  system: 0.1223
  reduce: 0.1223
  public: 0.1223

USR:
  support: 0.2357
  health: 0.1964
  need: 0.1468
  system: 0.1462
  investment: 0.1462
  economic: 0.1416
  public: 0.1391
  resource: 0.1370
  country: 0.1314
  education: 0.1314

PMP:
  support: 0.2550
  policy: 0.2211
  promote: 0.1796
  people: 0.1628
  energy: 0.1540
  romanian: 0.1519
  state: 0.1465
  european: 0.1411
  political: 0.1411
  movement: 0.1378

UDMR:
  hungarian: 0.3196
  transylvania: 0.2579
  percent: 0.2283
  propose: 0.2058
  good: 0.1741
  year: 0.1741
  support: 0.1741
  family: 0.1523
  community: 0.1523
  transylvanian: 0.1370
```

```
Top hand codes for each party:

PSD:
Code 504 - Welfare State Expansion: 183 times (15.6%)
Code 402 - Incentives: Positive: 134 times (11.4%)
Code 703.1 - Agriculture and Farmers: Positive: 116 times (9.9%)
Code 411 - Technology and Infrastructure: Positive: 90 times (7.7%)
Code 701 - Labour Groups: Positive: 80 times (6.8%)
Code 506 - Education Expansion: 50 times (4.3%)
Code 303 - Governmental and Administrative Efficiency: 32 times (2.7%)
Code NA - Not Applicable: 29 times (2.5%)
Code 502 - Culture: Positive: 29 times (2.5%)
Code 410 - Economic Growth: Positive: 27 times (2.3%)

PNL:
Code 411 - Technology and Infrastructure: Positive: 42 times (18.8%)
Code 402 - Incentives: Positive: 22 times (9.8%)
Code 303 - Governmental and Administrative Efficiency: 16 times (7.1%)
Code 504 - Welfare State Expansion: 15 times (6.7%)
Code 501 - Environmental Protection: 12 times (5.4%)
Code 502 - Culture: Positive: 11 times (4.9%)
Code 703.1 - Agriculture and Farmers: Positive: 11 times (4.9%)
Code 408 - Economic Goals: 10 times (4.5%)
Code 506 - Education Expansion: 10 times (4.5%)
Code 401 - Free Market Economy: 7 times (3.1%)

USR:
Code 411 - Technology and Infrastructure: Positive: 88 times (15.3%)
Code 504 - Welfare State Expansion: 71 times (12.3%)
Code 506 - Education Expansion: 58 times (10.1%)
Code 703.1 - Agriculture and Farmers: Positive: 48 times (8.3%)
Code 303 - Governmental and Administrative Efficiency: 31 times (5.4%)
Code 304 - Political Corruption: 28 times (4.9%)
Code 601.1 - National Way of Life General: Positive: 26 times (4.5%)
Code 502 - Culture: Positive: 26 times (4.5%)
Code 501 - Environmental Protection: 23 times (4.0%)
Code 701 - Labour Groups: Positive: 17 times (3.0%)

PMP:
Code 303 - Governmental and Administrative Efficiency: 34 times (8.3%)
Code 107 - Internationalism: Positive: 29 times (7.1%)
Code 506 - Education Expansion: 28 times (6.8%)
Code 501 - Environmental Protection: 28 times (6.8%)
Code 601.1 - National Way of Life General: Positive: 22 times (5.4%)
Code 108 - European Community/Union: Positive: 20 times (4.9%)
Code 305.1 - Political Authority: Party Competence: 20 times (4.9%)
Code 304 - Political Corruption: 19 times (4.6%)
Code 411 - Technology and Infrastructure: Positive: 19 times (4.6%)
Code 703.1 - Agriculture and Farmers: Positive: 17 times (4.1%)

UDMR:
Code 305.1 - Political Authority: Party Competence: 12 times (14.6%)
Code 506 - Education Expansion: 11 times (13.4%)
Code 504 - Welfare State Expansion: 10 times (12.2%)
Code 607.1 - Multiculturalism General: Positive: 8 times (9.8%)
Code 411 - Technology and Infrastructure: Positive: 7 times (8.5%)
Code 301 - Decentralization: 6 times (7.3%)
Code 703.1 - Agriculture and Farmers: Positive: 6 times (7.3%)
Code 412 - Controlled Economy: 3 times (3.7%)
Code 402 - Incentives: Positive: 3 times (3.7%)
Code 701 - Labour Groups: Positive: 2 times (2.4%)
```

```
Topic Modeling Results:
Total number of topics found: 11

Top topics per party:

PSD:
Topic: Economy Finance: tax, income, gdp, cass, lei
Topic: Youth Education: young, people, sport, programme, education
Topic: Healthcare: health, hospital, patient, medical, medicine

PNL:
Topic: Infrastructure: port, infrastructure, transport, project, motorway
Topic: Economy Finance: tax, income, gdp, cass, lei
Topic: Energy Environment: energy, forest, electricity, gas, power

USR:
Topic: Public Administration: public, administration, service, information, citizen
Topic: Healthcare: health, hospital, patient, medical, medicine
Topic: Education Reform: education, teacher, student, school, learn

PMP:
Topic: International Relations: partnership, strategic, promote, security, movement
Topic: Public Administration: public, administration, service, information, citizen
Topic: Culture Identity: cultural, culture, artist, heritage, nation

UDMR:
Topic: Regional Community: transylvania, community, family, good, child
Topic: International Relations: partnership, strategic, promote, security, movement
Topic: Culture Identity: cultural, culture, artist, heritage, nation
```

```
Detailed Topic Analysis:
   Party  Topic_ID                                                                                             Top_Words  Size
0    PSD         5                                    tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue    10
1    PSD         3                  young, people, sport, programme, education, hour, beneficiary, business, school, lei    11
2    PSD         0                health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei    13
3    PNL         6                port, infrastructure, transport, project, motorway, iasi, terminal, road, new, quality     6
4    PNL         5                                    tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue    10
5    PNL         4         energy, forest, electricity, gas, power, environmental, environment, plant, thermal, forestry    11
6    USR         1  public, administration, service, information, citizen, justice, economic, time, economy, institution    13
7    USR         0                health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei    13
8    USR         7        education, teacher, student, school, learn, university, teach, vocational, training, integrate     6
9    PMP         9     partnership, strategic, promote, security, movement, european, cooperation, sea, political, black     6
10   PMP         1  public, administration, service, information, citizen, justice, economic, time, economy, institution    13
11   PMP         8              cultural, culture, artist, heritage, nation, identity, promote, reform, regional, labour     6
12  UDMR        10                      transylvania, community, family, good, child, rail, modern, school, future, road     4
13  UDMR         9     partnership, strategic, promote, security, movement, european, cooperation, sea, political, black     6
14  UDMR         8              cultural, culture, artist, heritage, nation, identity, promote, reform, regional, labour     6
```

```
Processed PSD manifesto - 64015 characters
Processed PNL manifesto - 22552 characters
Processed USR manifesto - 63746 characters
Processed PMP manifesto - 38293 characters
Processed UDMR manifesto - 6362 characters
```

```
PSD Topic: Economy Finance: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue
PSD Topic: Youth Education: young, people, sport, programme, education, hour, beneficiary, business, school, lei
PSD Topic: Healthcare: health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei
PNL Topic: Infrastructure: port, infrastructure, transport, project, motorway, iasi, terminal, road, new, quality
PNL Topic: Economy Finance: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue
PNL Topic: Energy Environment: energy, forest, electricity, gas, power, environmental, environment, plant, thermal, forestry
USR Topic: Public Administration: public, administration, service, information, citizen, justice, economic, time, economy, institution
USR Topic: Healthcare: health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei
USR Topic: Education Reform: education, teacher, student, school, learn, university, teach, vocational, training, integrate
PMP Topic: International Relations: partnership, strategic, promote, security, movement, european, cooperation, sea, political, black
PMP Topic: Public Administration: public, administration, service, information, citizen, justice, economic, time, economy, institution
PMP Topic: Culture Identity: cultural, culture, artist, heritage, nation, identity, promote, reform, regional
```

```
Sentiment Analysis Summary:
   Party                                                                                           Topic_Words  Num_Sentences  Avg_Compound  Avg_Positive  Avg_Negative  Avg_Neutral
0    PSD                                    tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue            209         0.252         0.093         0.024        0.883
1    PSD                  young, people, sport, programme, education, hour, beneficiary, business, school, lei            211         0.326         0.112         0.017        0.871
2    PSD                health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei            180         0.281         0.092         0.025        0.883
3    PNL                port, infrastructure, transport, project, motorway, iasi, terminal, road, new, quality             61         0.390         0.144         0.018        0.838
4    PNL                                    tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue             37         0.293         0.121         0.026        0.854
5    PNL         energy, forest, electricity, gas, power, environmental, environment, plant, thermal, forestry             38         0.420         0.158         0.018        0.824
6    USR  public, administration, service, information, citizen, justice, economic, time, economy, institution            180         0.417         0.159         0.032        0.809
7    USR                health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei            106         0.360         0.148         0.035        0.817
8    USR        education, teacher, student, school, learn, university, teach, vocational, training, integrate            199         0.430         0.173         0.036        0.791
9    PMP     partnership, strategic, promote, security, movement, european, cooperation, sea, political, black            107         0.469         0.208         0.035        0.757
10   PMP  public, administration, service, information, citizen, justice, economic, time, economy, institution            103         0.415         0.211         0.040        0.749
11   PMP              cultural, culture, artist, heritage, nation, identity, promote, reform, regional, labour            118         0.388         0.189         0.043        0.767
12  UDMR                      transylvania, community, family, good, child, rail, modern, school, future, road             41         0.367         0.169         0.008        0.823
13  UDMR     partnership, strategic, promote, security, movement, european, cooperation, sea, political, black              4         0.437         0.147         0.015        0.838
14  UDMR              cultural, culture, artist, heritage, nation, identity, promote, reform, regional, labour              8         0.331         0.142         0.013        0.845
```


## Most Significant Sentences by Party:

```
PSD:
Most Negative:
Topic: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue...
Sentence: VAT refunds) LOWEST TAX BURDEN DEADLINE: 5 YEARSConsolidate the first position of the lowest tax burden in the European Union by reaching the EU minimum level for excise duties and VAT
Scores: Compound=-0.893, Pos=0.045, Neg=0.310

Most Positive:
Topic: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue...
Sentence: MODERNIZATION OF ADJACENT PORTS Port Mangalia, Port Basarabi, Port Ovidiu, Port Medgidia OTOPENI AIRPORT NEW PASSENGER TERMINAL 250 m², level of service B MODERNIZATION RUNWAY 1 Rehabilitation of taxiway with increased strength (PCN from 74 to 85 for heavy aircraft), New beaconing 2 new ILS EXTENSION OF AIRCRAFT STATIONING PLATFORM 17,000 m2 DEVELOPMENT OF ADJACENT ROAD INFRASTRUCTURE New long-term parking, Bus and minibus terminal TAROM COMPANY COST OPTIMIZATION Purchase of 30 new fuel-efficient aircraft, Standardization of fleet to reduce maintenance costs, Online system directly on Tarom website, no intermediaries PERSONNEL OPTIMIZATION Personnel evaluation, Salary increases in certain departments INCREASE MARKET SHARE Development of marketing department, New domestic and international charter flights, New passenger facilities, Technical department to provide maintenance for other companies as well ENVIRONMENTAL INFRASTRUCTURE SUSTAINABLE FOREST DEVELOPMENT WHAT ARE WE GOING TO DO
Scores: Compound=0.991, Pos=0.271, Neg=0.013

Most Neutral:
Topic: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue...
Sentence: Lei Economic growth*5
Scores: Compound=0.000, Pos=0.000, Neg=0.000
```

```
PNL:
Most Negative:
Topic: tax, income, gdp, cass, lei, budget, taxis, pay, employee, revenue...
Sentence: 50% reduction in the number of taxes *Reduce/eliminate the administrative costs of tax policy by eliminating taxes with low tax efficiency but with a negative impact on the total tax burden
Scores: Compound=-0.874, Pos=0.073, Neg=0.273

Most Positive:
Topic: port, infrastructure, transport, project, motorway, iasi, terminal, road, new, quality...
Sentence: Coordinate transport infrastructure with national development poles to stimulate economic growth and investment in industries and services, and strengthen regional hubs in Bucharest, Constanta, Timisoara, Suceava, Brasov through interconnectivity with all modes of transport: Completion of the rehabilitation works on the railway infrastructure of the European Corridor IV (Priority Project 22 Curtici - Simeria - Sighisoara - Brasov - Bucharest - Constanta) and the start of the rehabilitation works on the railway infrastructure of the European Corridor IX (Bucharest - Iasi - Ungheni) Interconnectivity of express roads and county roads with the main national motorways to balance rapid access in all areas of the country Balanced distribution of transport on all types of infrastructure (road, rail, sea, air) 47
Scores: Compound=0.961, Pos=0.170, Neg=0.000

Most Neutral:
Topic: port, infrastructure, transport, project, motorway, iasi, terminal, road, new, quality...
Sentence: 100 liberal measures in addition to the projects presented by Dacian Ciolos through the Romania 100 Platform PNL proposes 100 liberal measures in addition to the projects presented by Dacian Ciolos through the Romania 100 Platform
Scores: Compound=0.000, Pos=0.000, Neg=0.000
```

```
USR:
Most Negative:
Topic: education, teacher, student, school, learn, university, teach, vocational, training, integrate...
Sentence: Unhappy, demotivated and financially burdened teachers cannot produce happy, high-achieving children
Scores: Compound=-0.818, Pos=0.000, Neg=0.515

Most Positive:
Topic: health, hospital, patient, medical, medicine, doctor, disease, service, programme, lei...
Sentence: We propose increasing the share of financial allocations for the development of family medicine, equipping it with the necessary medical equipment and providing financial incentives for doctors to invest in their own practices in order to encourage team-building in shared practices, especially in rural and remote areas, thus applying a successful model that would bring high efficiency in the health system, increased patient satisfaction and a reduction of pressure on hospital resources
Scores: Compound=0.963, Pos=0.272, Neg=0.025

Most Neutral:
Topic: public, administration, service, information, citizen, justice, economic, time, economy, institution...
Sentence: the stabilization of electoral lists in correlation with the stabilization of data from the National Register of Persons
Scores: Compound=0.000, Pos=0.000, Neg=0.000
```

```
PMP:
Most Negative:
Topic: partnership, strategic, promote, security, movement, european, cooperation, sea, political, black...
Sentence: We will fight with ideas and arguments against defeatism, mockery of national and European values, or the cult of undervaluation
Scores: Compound=-0.735, Pos=0.098, Neg=0.359

Most Positive:
Topic: partnership, strategic, promote, security, movement, european, cooperation, sea, political, black...
Sentence: The People's Movement supports the need to develop the economic dimension of the Romanian foreign policy, both by supporting the presence of Romanian companies globally, but also to attract investment in Romania, with emphasis on signalling business opportunities, attracting foreign investors, promoting Romanian products
Scores: Compound=0.967, Pos=0.370, Neg=0.000

Most Neutral:
Topic: partnership, strategic, promote, security, movement, european, cooperation, sea, political, black...
Sentence: We will depoliticise the state, adopting as a general rule political appointments exclusively at the level of Minister and Secretary of State and their cabinets
Scores: Compound=0.000, Pos=0.000, Neg=0.000
```

```
UDMR:
Most Negative:
Topic: transylvania, community, family, good, child, rail, modern, school, future, road...
Sentence: But just as we know that we are not perfect, we are also aware that there is still a lot to do
Scores: Compound=-0.612, Pos=0.000, Neg=0.160

Most Positive:
Topic: transylvania, community, family, good, child, rail, modern, school, future, road...
Sentence: 6 The education law must be implemented urgently: pupils in Hungarian classes must learn Romanian according to a special curriculum, with a special textbook, in all 12 years of school education, because it is in their interest to learn Romanian flawlessly
Scores: Compound=0.922, Pos=0.303, Neg=0.000

Most Neutral:
Topic: transylvania, community, family, good, child, rail, modern, school, future, road...
Sentence: Transylvania, the future for all of us
Scores: Compound=0.000, Pos=0.000, Neg=0.000
```


```
Enter a word to search for (or 'quit' to exit): pension

Searching for the lemmatized word 'pension' in all manifestos:
Found in PSD's manifesto (19 times)
Found in PNL's manifesto (2 times)
Found in USR's manifesto (1 times)
Found in PMP's manifesto (2 times)
Found in UDMR's manifesto (3 times)

Enter a word to search for (or 'quit' to exit): justice

Searching for the lemmatized word 'justice' in all manifestos:
Found in PSD's manifesto (1 times)
Found in PNL's manifesto (1 times)
Found in USR's manifesto (6 times)
Found in PMP's manifesto (10 times)

Enter a word to search for (or 'quit' to exit): corruption

Searching for the lemmatized word 'corruption' in all manifestos:
Found in USR's manifesto (11 times)
Found in PMP's manifesto (6 times)

Enter a word to search for (or 'quit' to exit): education

Searching for the lemmatized word 'education' in all manifestos:
Found in PSD's manifesto (29 times)
Found in PNL's manifesto (5 times)
Found in USR's manifesto (34 times)
Found in PMP's manifesto (21 times)
Found in UDMR's manifesto (5 times)

Enter a word to search for (or 'quit' to exit): health

Searching for the lemmatized word 'health' in all manifestos:
Found in PSD's manifesto (23 times)
Found in PNL's manifesto (2 times)
Found in USR's manifesto (43 times)
Found in PMP's manifesto (6 times)


Enter a word to search for (or 'quit' to exit): quit
```
