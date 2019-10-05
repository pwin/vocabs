This is work to prepare a core catalogue of public bodies in Scotland

It is based on the EC CPOV - https://github.com/SEMICeu/CPOV

Things to take into account:

* Italian work - https://github.com/italia/daf-ontologie-vocabolari-controllati/tree/master/Ontologie/COV 

[Visualisation of copv-ap-scot.owl](http://www.visualdataweb.de/webvowl/#iri=https://raw.githubusercontent.com/pwin/vocabs/master/legalEnts/CPOV/CPOV-AP-SCOT-v1/copv-ap-scot.owl)



Resources;

* http://ukgovld.github.io/ukgovldwg/recommendations/uri-patterns.htm
* https://philarcher.org/diary/2013/uripersistence/
* https://innovation.thomsonreuters.com/content/dam/openweb/documents/pdf/corporate/Reports/creating-value-with-identifiers-in-an-open-data-world.pdf

* https://github.com/weso/landportalDoc/wiki/URI-Scheme

Other useful links;

*  https://confluence.csiro.au/public/VOCAB/vocabulary-services/publishing-vocabularies/best-practice-in-formalizing-a-skos-vocabulary
*  http://smethur.st/posts/176135860


## URI Patterns 

{protocol}://{base uri}/{type}/{sector}/{domain}/{id of resource}

#### type: cat; def; kos; res; doc; api; web, id

| type | description |
| :---- | :---- |
| cat | catalogue (e.g. DCAT catalogue) |
| def | schemas - e.g. OWL or RDFS |
|kos | concept scheme e.g. SKOS or SKOS/XL|
|id |  resource - e.g. real world object|
|doc | document (including web page)|
|api | entry point to an API|
|web | website home page|


#### Sector: could represent the org or the community

| Domain | info | 
| :--- | :--- |
| gov  | Scottish Government etc |
| hsc  | Health and Social Care  |
| edu  | SQA, Skills, Education |
| reg  | Regulator, Inspection domains  |
| gen  | general |




