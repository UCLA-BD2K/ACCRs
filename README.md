# ACCRs 
This repository contains documentation for the set of Annotated Clinical Case Reports (ACCRs) along with associated scripts for processing and verification of annotation metadata.

Data files are not provided in this repository but are available on Figshare at **TBD**.
They are described in brief here.

## Annotation Guide
An annotation guide is provided in ***Annotation_Guide.md*** for the purposes of understanding creation of the ACCR set.

## ACCR Data Files
### Data Set
This file, ***ACCRs.tsv***, contains the full ACCR data set.

All annotation data are provided in this file. This is a tab-delimited file of 58 columns, one header row, and 3,000 rows of data, where each row provides metadata and annotations for a single clinical case report (CCR).

Please see the ACCR File Guide (***ACCR_File_Guide.md***) in this repository for details of all features provided in ***ACCRs.tsv***.

### Citations
Citations for all clinical case reports used in the assembly of the ACCR set are available in the file ***ACCR_citations.bib***. This file is in [BibTeX format](http://www.bibtex.org/Format/).

### Annotation Template
The annotation template is available at in ***TEMPLATE.xlsx***. This is an Excel format spreadsheet; we have found this format to be easiest for annotators to use. 

### Rare Mitochondrial Disease Subset
The Rare Mitochondrial Disease, or RMD, subset of the ACCRs includes 246 reports concerning a selection of seven diseases with mitochondrial etiologies. This subset includes two tab-delimited files: ***ACCR_RMD_ICD10.tsv***, or the code file, and ***ACCR_RMD_ICD10_Categories.tsv***, the category file. Both files contain a header row, values corresponding to a sincle CCR per subsequent row, an identifying PubMed ID in the first column, and the name of a RMD in the second column. In the code file, each subsequent column provides a binary value indicating whether the [ICD-10-CM code](https://www.cdc.gov/nchs/icd/icd10cm.htm) in the header row is appropriate for the events described within the CCR. In the categories file, the header row contains names of 20 chapters of the ICD-10-CM codes, with values indicating whether at least one code in the corresponding code block has a value of '1' in the code file.

### MeSH Term List
A list of all MeSH terms, with one unique term per list, is available in the tab-delimited file ***ACCR_mesh.tsv***. Each row includes a single MeSH term (as per the [2018 MeSH Terminology](https://www.nlm.nih.gov/mesh/filelist.html)) in the first column and a single letter indicating the corresponding section of the [MeSH Tree](https://meshb.nlm.nih.gov/treeView).

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
