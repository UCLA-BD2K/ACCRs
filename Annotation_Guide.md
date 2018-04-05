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
* Title. The title of the document. For consistency, this should be identical to the title used in the PubMed citation. Example: *Case report: a case of severe illness.*
* Authors. The authors of the document. For consistency, this should be identical to the author format used in the PubMed citation but separated with semicolons, such that *Firstname A. Lastname, Authortwo B. Secondlastname* is rendered as this example: *Lastname FA;Secondlastname AB*
* Year. The year of publication of the document. For consistency, this should be identical to the year specified in the PubMed citation. Example: *1994*
* Journal. The full title of the journal in which the document was published, as specified by the NLM Catalog (https://www.ncbi.nlm.nih.gov/nlmcatalog). For example, the "International journal of cardiology" should not be specified as *Int J Cardiol* or as *Int. J. Cardiol.* but rather as *International journal of cardiology*. "The" should be omitted from the prefix of journal names, such that *The Lancet* is rendered as *Lancet*.
* Institution. The address of the home institution of the authors of the document, as specified in the document. This may include departments, geographic locations, and postal address details. If multiple locations are provided (e.g., if affiliations differ between authors), specify only details for the corresponding author. If a corresponding author cannot be identified, use that of the first author, or do not specify an institution. If a corresponding author has multiple affiliations, specify both and separate using semicolons. Examples: *Department of paediatrics, Division of paediatric cardiology, London Health Sciences Centre, London, Ontario, Canada*; *Department of Dermatology, University of California, 1701 Divisadero St, 3rd Floor, San Francisco, CA 94115, USA*
* Corresponding Author. (Internal use). This field may be used to identify a corresponding author for the document, as specified within the document heading. This author name should take the same format as that used in the Authors data type. Example: *Lastname FA*
* PMID. Identical to that specified above. Example: *29999555*
* DOI. A Digital Object Identifier, resolvable to the document (through https://www.doi.org/) and provided by the publisher. The DOI should refer to the URL of the document as provided by the publisher, not a PubMed Central page. DOIs may not be available for all documents. Example: *10.3928/00904481-20155555-03* (not a real DOI)
* Link. A stable URL to the full text of the document, generally the PubMed Central version for purposes of consistency.
* Language(s)

## Medical content (Accessable, Interoperable, Reusable)
* Key Words
* Demography
* Geographic Locations 
* Life Style
* Medical History Taking-Family history
* Social Work
* Medical History Taking-Medical/surgical history
* Disease System
* Signs and Symptoms
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

