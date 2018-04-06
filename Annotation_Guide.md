# Annotation Guide for Annotated Clinical Case Reports (ACCRs)

## Introduction
This Guide contains a list of data types identified in the process of assembling the ACCR data set, along with guidelines for what types of text or numerical values should be used in each type. We have arranged the types into four general categories: document and annotation indentification values, case report identification values (i.e., document-level properties), medical content concepts (for the most part, these are concept-level properties) and acknowledgements (i.e., text within each document linking it to other organizations and publications). A single set of values corresponds to those identified in a single document.

As this guide primarily describes how to annotate clinical case reports, the data types listed here are those we have determined to be most descriptive for clinical case reports and patient-focused medical documents in general. Our goal is also to follow FAIR principles in establishing structure on case report text and have identified the corresponding principles in two of the categories provided below. We encourage using these data types to annotate new sets of documents and/or to build new ontologies.

Data types without corresponding values in a given document may be left blank or specified as "NA". For most fields, unless specified otherwise, separate values are separated by semicolons. This is compatible with semicolons contained within original text in that the punctuation already denotes a distinct concept or idea.

Fields marked as (internal use) are those not provided with the ACCR set but designed for focused tasks.

## Scoring

## Document and Annotation Identification
* PMID. Each published document should have a PubMed identifier unless it is not available through PubMed. Example: *29999555*
* Citation. (Internal use). This field may be used to track citation count for the document, as determined by PubMed Central, Google Scholar, Web of Science, or other indexing system providing citation records. Example: *5*
* Access date (Internal use). This field may be used to specify the date on which a document was read and annotated. The exact format of this date is not critical but should be consistent between annotations. Example: *6/28/2017*

## Case Report Identification (Findable)
Values in this category provide document-level features.

* Title. The title of the document. For consistency, this should be identical to the title used in the PubMed citation. Example: *Case report: a case of severe illness.*
* Authors. The authors of the document. For consistency, this should be identical to the author format used in the PubMed citation but separated with semicolons, such that *Firstname A. Lastname, Authortwo B. Secondlastname* is rendered as this example: *Lastname FA;Secondlastname AB*
* Year. The year of publication of the document. For consistency, this should be identical to the year specified in the PubMed citation. Example: *1994*
* Journal. The full title of the journal in which the document was published, as specified by the NLM Catalog (https://www.ncbi.nlm.nih.gov/nlmcatalog). For example, the "International journal of cardiology" should not be specified as *Int J Cardiol* or as *Int. J. Cardiol.* but rather as *International journal of cardiology*. "The" should be omitted from the prefix of journal names, such that *The Lancet* is rendered as *Lancet*.
* Institution. The address of the home institution of the authors of the document, as specified in the document. This may include departments, geographic locations, and postal address details. If multiple locations are provided (e.g., if affiliations differ between authors), specify only details for the corresponding author. If a corresponding author cannot be identified, use that of the first author, or do not specify an institution. If a corresponding author has multiple affiliations, specify both and separate using semicolons. Examples: *Department of paediatrics, Division of paediatric cardiology, London Health Sciences Centre, London, Ontario, Canada*; *Department of Dermatology, University of California, 1701 Divisadero St, 3rd Floor, San Francisco, CA 94115, USA*
* Corresponding Author. (Internal use). This field may be used to identify a corresponding author for the document, as specified within the document heading. This author name should take the same format as that used in the Authors data type. Example: *Lastname FA*
* PMID. Identical to that specified above. Example: *29999555*
* DOI. A Digital Object Identifier, resolvable to the document (through https://www.doi.org/) and provided by the publisher. The DOI should refer to the URL of the document as provided by the publisher, not a PubMed Central page. DOIs may not be available for all documents. Example: *10.3928/00904481-20155555-03* (not a real DOI)
* Link. A stable URL to the full text of the document, generally the PubMed Central version for purposes of consistency.
* Language(s). (Internal use). This field may be used to identify a document's primary language. Example: *english*

## Medical content (Accessable, Interoperable, Reusable)
Values in this category identify document-level, concept-level, and text-level features. These features provide ways to observe conceptual and semantic similarities between document contents, with a focus on medical topics and events. Most categories in this section can include multiple text statements and each should be separated using semicolons. In general, include sufficient detail to contextualize each statement (i.e., do not limit all terms to a controlled vocabulary) but do not include extensive detail beyond each obervation, e.g. omit phrases such as "the patient presented with" unless these details are semantically crucial to the statement's meaning.

* Key Words. Specific terms identified within a document, usually in its header, as key terms. Separate by semicolons. May be identical to MeSH terms provided through PubMed. Example: *barth syndrome; cardiomyopathy; 3-methylglutaconic acid*
* Demography. Values provided here should be any text statements describing the patient's background, including sex (sometimes referred to as gender, though the terms are not identical), age, ethnicity, or nationality. In practice, this nearly always includes age and sex, though the document may not provide these or further details. Unprocessed example: *46-year-old; female*

  In the ACCR set, this field is processed further into Age and Gender using regular expressions to account for differences in formatting. Processing follows the following rules; these may be used as part of a processing script or used consistently in the course of manual annotation. 

  1. Ages are integers indicating number of years of age. Ages expressed as words (e.g. *twelve*) are converted to integers.
  2. Patients less than 1 year of age are assigned an age of 0.
  3. If a decade category of age is provided, estimate the patient's age to be in the middle of the decade, e.g. a patient in his or her *50's* or *fifties* is estimated to be 55.
  4. Where specified, sex should be annotated as *male* or *female*. This binary categorization may be expanded as needed.

* Geographic Locations. Values should be any text terms or phrases denoting physical locations (i.e., not biological locations) other than those directly identifying the institution corresponding to the clinical presentation. This may include any geographic locale where the patient lives or has traveled to recently. Example: *born in Penteado, Alagoas, Brazil and residing in São Paulo*

* Life Style. Values should include any text statements describing frequent patient activities or behaviors relevant to their general health. In practice, this frequently involves smoking or alcohol consumption habits, but may also include sun exposure, diet, or frequency of specific types of physical activity. Examples: *nonsmoker*, *drank alcohol in moderation*, *was physically active*

* Medical History Taking-Family history. Values should include any text statements describing clinical observations of and events experienced by siblings, parents, and other family members. This includes genetic conditions and negative observations (i.e. *family history was negative for* a disease). Examples: *her mother had breast cancer at age 40*, *non-consanguineous parents with an uneventful perinatal history*, *she had family members with g6pd deficiency*.

* Social Work. Values should include any text statements describing patient background not covered in Demography or Life Style, though there may be overlaps in content between these categories. The statements may include occupational history and social habits. Examples: *college student*, *divorced with two children*, *he had been incarcerated for years*

* Medical History Taking-Medical/surgical history. Values should include any text statements describing any medical observations or events taking place prior to the beginning of the clinical presentation. This includes obstetric history and periods of good health. Treatments should also be included. Examples:

  *excessive fatigue; oppression over the chest; right-sided hemicolectomy; low-differentiated adenocarcinoma of the caecum; hypertension; capecitabine (five 500 mg oral tablets twice daily); chemotherapy*

  *with a 3-year history of chronic obstructive pulmonary disease; he had been diagnosed with stage I low-grade prostate cancer several years previously*

* Disease System. Unlike the largely free-text values used elsewhere in the Medical Content, values for Disease System are at least one of 16 categories indicating disease type and organ system involvement, separated by semicolons. Categories are not comprehensive but should indicate most systems impacted by the events described in the clinical presentation and diagnosed disease. The values should be specified as follows, with additional details in parentheses:
  1. *cancer* (Any type of cancer or malignant neoplasm)
  2. *nervous* (Also referred to as Neuronal Disease or Nervous System Diseases. Includes any disease of the brain, spine, or nerves)
  3. *cardiovascular* (Also referred to as Cardiovascular Diseases.)
  4. *musculoskeletal and rheumatic* (Also referred to as Musculoskeletal Diseases and Rheumatological Diseases.)
  5. *digestive* (Also referred to as
  6. *obstetrical and gynecological* (Also referred to as Digestive Diseases or Digestive System Diseases.)
  7. *infectious* (Also referred to as Infectious Diseases.)
  8. *respiratory* (Also referred to as Respiratory Diseases or Respiratory Tract Diseases.)
  9. *hematologic* (Also referred to as Hematologic Diseases.)
  10. *kidney and urologic* (Also referred to as Kidney Diseases and Urologic Diseases.)
  11. *endocrine* (Also referred to as Endocrine Diseases.)
  12. *oral and maxillofacial* (Also referred to as Oral and Maxillofacial Diseases. Includes all dental and craniofacial pathologies)
  13. *eye* (Also referred to as Ophthalmological Diseases. Includes visual disturbances and blindness)
  14. *otorhinolaryngologic* (Also referred to as Otorhinolaryngologic Diseases.)
  15. *skin* (Also referred to as Skin Diseases.)
  16. *rare* (A special category reserved for reports of rare diseases, defined as those impacting fewer than 200,000 individuals in the United States; see https://rarediseases.info.nih.gov/diseases) 
  
  Example: *cancer; skin; oral and maxillofacial* are used for a case entitled "Cutaneous horn: case report." (Akram et al. 2011, PMID 20226577). 
  
  These categories may be expanded to include additional groups or specific disease, e.g. in the ACCR set, we have included a *mitochondrial rare* category to denote reports of rare mitochondrial diseases along with names of these diseases.
  
* Signs and Symptoms. Values should include any text statements describing any medical observations of signs or symptoms beginning at initial presentation but not including those in the outcome. May overlap with other types if symptoms continue from history to initial presentation. Examples:

  *headaches; confusion; photophobia; neck stiffness; pyrexia (38.5 degrees C) and bilateral third nerve palsies*

  *a papulo-pustular rash and Raynaud’s phenomenon; extreme fatigue, pale stools, dark urine and pruritus*

* Comorbidity
* Diagnostic Techniques and Procedures
* Diagnosis
* Laboratory Values
* Pathology
* Drug Therapy
* Therapeutics
* Patient Outcome Assessment
* Diagnostic Imaging/Videotape Recording
* Relationship to other Case Reports
* Relationship with Clinical Trial
* Crosslink with Database

## Acknowledgements
* Funding source
* Award number
* Disclosures/Conflict of interest
* References

