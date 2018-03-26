# ACCRs 
This repository contains a set of Annotated Clinical Case Reports (ACCRs) along with associated scripts for processing and verification of annotation metadata. 

## Data Set
The full ACCR data set is provided in the folder *Data*.
All annotation data are provided in the file ***ACCRs.tsv***. This is a tab-delimited file of 60 columns, one header row, and 3,000 rows of data, where each row provides metadata and annotations for a single clinical case report (CCR).

Please see ***ACCR_guide.md*** for explanations of all features provided in the ACCR data set.

## Annotation Template
The annotation template is provided within the folder *Template* in the file ***TEMPLATE.xlsx***. For consistency and interoperability, we recommend that all newly created annotation files use a filename of the following format:

CCR[index]-[PMID]-metadata-[annotator].xlsx

where 

[index] is a unique numberical value specific to this annotation file, 

[PMID] is the PubMed idenfifier of the annotated document, and

[annotator] is the initials of the individual preparing the annotation.

## Processing
Scripts for processing a set of annotation documents prepared using the annotation template are provided within the folder *Processing*. Both scripts, ***Extract.py*** and ***ExtractFunctions.py***, should be placed within and run from the same directory as a folder entitled "AnnotatedFiles" (alternatively, edit the inputDirectoryPath value of Extract.py to use a different folder name).

These scripts are compatible with Python 2 and 3. They require the following Python packages, installable through *pip*:
* **openpyxl**
* **word2number**
* **unicodecsv**
* **xlrd**
* **pandas**
* **numpy**

These scripts were developed by Sarah Spendlove.

## Verification
Scripts for verifying a processed set of annotation documents are provided within the folder *Verification*.

These scripts were developed by Clement Feyt.

## Additional Resources
Please see also:
* [heartCases](https://github.com/caufieldjh/heartCases), an automated system for retreiving and working with MEDLINE-indexed clinical case reports

## Citation
Caufield et al. Manuscript in preparation.
