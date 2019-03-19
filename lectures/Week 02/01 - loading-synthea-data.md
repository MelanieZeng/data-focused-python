---
toc: true
toc_sticky: true
toc_label: "Page Contents"
toc_icon: "cog"
---
## Loading Synthea Data

Here we'll walk through the different data files from the [synthea](https://github.com/synthetichealth/synthea) data generator. Synthea can generate data in a number of formats including:
* CCDA
* CSV
* FHIR
* text


```python
with open('data/csv/providers.csv') as f:
    for line in f.readlines():
        print(line)
```

    Id,ORGANIZATION,NAME,GENDER,SPECIALITY,ADDRESS,CITY,STATE,ZIP,UTILIZATION
    
    30ee89ff-1932-4e7d-8358-7f84527f622e,8074c9c5-982f-3d30-8a5f-95f6ba9fde06,Del587 Williamson769,M,GENERAL PRACTICE,1400 LOCUST STREET,PITTSBURGH,PA,15219,2501,
    
    2570b996-8b89-417a-a661-a66c22e84b07,797d87ed-77fa-3b01-b971-0399bb10dc09,Bethany501 Windler79,F,GENERAL PRACTICE,3459 5TH AVENUE,PITTSBURGH,PA,15213,8,
    



```python
with open('data/FHIR/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.json') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: {
    
    1:   "resourceType": "Bundle",
    
    2:   "type": "transaction",
    
    3:   "entry": [
    
    4:     {
    
    5:       "fullUrl": "urn:uuid:4aaeea96-ef44-4d86-a313-ed9658b91618",
    



```python
with open('data/ccda/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.xml') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: <?xml version="1.0" encoding="UTF-8"?>
    
    1: <ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 http://xreg2.nist.gov:8080/hitspValidation/schema/cdar2c32/infrastructure/cda/C32_CDA.xsd">
    
    2:   <realmCode code="US"/>
    
    3:   <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
    
    4:   <templateId root="2.16.840.1.113883.10.20.22.1.1" extension="2015-08-01"/>
    
    5:   <templateId root="2.16.840.1.113883.10.20.22.1.2" extension="2015-08-01"/>
    



```python
with open('data/text/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.txt') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: Augustine565 Conroy74
    
    1: =====================
    
    2: Race:                Asian
    
    3: Ethnicity:           Non-Hispanic
    
    4: Gender:              F
    
    5: Age:                 49
    

