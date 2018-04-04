# ACCRs 
This repository contains documentation for the set of Annotated Clinical Case Reports (ACCRs) along with associated scripts for processing and verification of annotation metadata.

## Data Set
The full ACCR data set, as well as the associated citations, are available at **TBD**. They are not provided here.

All annotation data are provided in the file ***ACCRs.tsv***. This is a tab-delimited file of 60 columns, one header row, and 3,000 rows of data, where each row provides metadata and annotations for a single clinical case report (CCR).

Please see ***ACCR_guide.md*** for explanations of all features provided in the ACCR data set.

## Annotation Template
The annotation template is available at **TBD**. For consistency and interoperability, we recommend that all newly created annotation files use a filename of the following format:

CCR[index]-[PMID]-metadata-[annotator].xlsx

where 

[index] is a unique numberical value specific to this annotation file, 

[PMID] is the PubMed idenfifier of the annotated document, and

[annotator] is the initials of the individual preparing the annotation.

## Annotation Guide
An annotation guide is provided in ***Annotation_Guide.md*** for the purposes of understanding creation of the ACCR set, creation of new annotation sets similar to those within the ACCR set, and identification of features common to clinical case reports.

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
Scripts for verifying a processed set of annotation documents are provided within the folder *Verification*. The R script ***QualityControl.R*** should be run within the same directory as the processed annotation set (i.e., ACCRs.tsv). The functions within the script assume the existence of a comma-delimited annotation plan file containing, for each annotated record, the corresponding PMID and annotator. This allows for isolation of errors in the annotation process regarding target corpus coverage. Here, we have provided a blank annotation plan (***AnnotationPlan.csv***).

These scripts were developed by Clement Feyt.

## Geolocation Analysis
Scripts for visualizing the geographic distribution of a set of CCRs, based off locations indicated by their metadata and annotations, are provided in the folder *Geographic*.

These scripts were developed by Kitu Komya and Clement Feyt.

See also https://github.com/Key2-Success/HeartBD2K-Geographic-Data.

## Term-based Analysis
Scripts for preforming a term-based analysis of a set of processed, annotated CCRs are provided in the folder *Term Analysis*.

## Additional Resources
Please see also:
* [heartCases](https://github.com/caufieldjh/heartCases), an automated system for retreiving and working with MEDLINE-indexed clinical case reports

## Citation
Caufield et al. Manuscript in preparation.
