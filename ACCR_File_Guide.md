# Guide to Contents of the Annotated Clinical Case Reports (ACCRs) Data File

## Introduction
This Guide contains a list of data types contained within the ACCR data set. Most of these values correspond to those described as part of the annotation process; see the file ***Annotation_Guide.md*** for further details.

Fields may contain values of "NA" if no corresponding value for this category was found in or corresponding to a given document.

If not otherwise specified, values are those obtained from manual annotation, post-processed, and cleaned as specified in the Annotation Guide. For Disease Category columns, values are binary, with 1 indicating membership in the category and 0 indicating non-membership.

## ACCR Data File contents
Column | Title | Contents
--- | --- | ---
1 | *blank* | A number from zero to 2999 serving as an internal file index.
2 | CR Number | Internal ID. See Annotation Guide.
3 | Access Date | See Annotation Guide.
4 | Total Score | Sum of all scores for the full text document. See "Scoring and Template Usage" in Annotation Guide.
5 | Identification Score | Sum of all scores in the Document and Annotation Identification section for the full text document. See "Scoring and Template Usage" in Annotation Guide.
6 | Title | See Annotation Guide.
7 | Authors | See Annotation Guide.
8 | Year | Publication year. See Annotation Guide.
9 | Journal | Document source. See Annotation Guide.
10 | Institution | Affiliation of the corresponding author. See Annotation Guide.
11 | PMID | PubMed identifier of the document. See Annotation Guide.
12 | DOI | Digital Object Identifier of the document. See Annotation Guide.
13 | Link | URL to the document; generally through doi.org. If a DOI is not available, may take other formats. See Annotation Guide.
14 | Medical Content Score | Sum of all scores in the Medical Content section for the full text document. See "Scoring and Template Usage" in Annotation Guide.
15 | Keywords | See Annotation Guide.
16 | Geographic Locations | See Annotation Guide.
17 | Life Style | See Annotation Guide.
18 | Family History | See Annotation Guide.
19 | Social History | See Annotation Guide.
20 | Medical/Surgical History | See Annotation Guide.
21 | Signs and Symptoms | See Annotation Guide.
22 | Comorbidities | See Annotation Guide.
23 | Diagnostic Techniques and Procedures | See Annotation Guide.
24 | Diagnosis | See Annotation Guide.
25 | Laboratory Values | See Annotation Guide.
26 | Pathology | See Annotation Guide.
27 | Pharmacological Therapy | See Annotation Guide.
28 | Interventional Therapy | See Annotation Guide.
29 | Patient Outcome Assessment | See Annotation Guide.
30 | Acknowledgements Score | Sum of all scores in the Acknowledgements section for the full text document. See "Scoring and Template Usage" in Annotation Guide.
31 | Funding Source | See Annotation Guide.
32 | Award Number | See Annotation Guide.
33 | Disclosures | See Annotation Guide.
34 | References | Count of references included in the document. See Annotation Guide.
35 | Age | Numerical age in number of years. Patients less than one year of age are assigned an age value of zero. Determined from Demography annotation.
36 | Gender | May be Male, Female, or NA. Determined from Demography annotation.
37 | Cancer | Disease category.
38 | Nervous System Diseases | Disease category.
39 | Cardiovascular Diseases | See Annotation Guide.
40 | Musculoskeletal Diseases and Rheumatological Diseases | Disease category.
41 | Digestive System Diseases | Disease category.
42 | Obstetrical and Gynecological Diseases | Disease category.
43 | Infectious Diseases | Disease category.
44 | Respiratory Tract Diseases | Disease category.
45 | Hematologic Diseases |Disease category.
46 | Kidney Diseases and Urologic Diseases | Disease category.
47 | Endocrine System Diseases | Disease category.
48 | Oral and Maxillofacial Diseases | Disease category.
49 | Ophthalmological Diseases | Disease category.
50 | Otorhinolaryngologic Diseases | Disease category.
51 | Skin Diseases | Disease category.
52 | Rare Diseases | Disease category.
53 | AllDiseaseSystems | Set of all disease categories assigned to the document, as terms. 
54 | Images | Count of clinical images in the document, not counting supplements.
55 | Graphs or Illustrations | Count of prepared graphs, figures, and illustrations in the document, not counting supplements.
56 | Videos | Count of videos and animations provided with the document.
57 | Tables | Count of tables in the document, not counting supplmentary tables.
58 | Contributor | Two-letter initials of the annotator for this document.


