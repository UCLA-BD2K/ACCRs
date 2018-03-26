from ExtractFunctions import *


inputDirectoryPath = "AnnotatedFiles/"

i=0
tmpList = []
for f in os.listdir(inputDirectoryPath):   
    i = i+1
    print(str(i) + " : " + f)
    tmpList.append(getDataFile(inputDirectoryPath, f))

columnNamesOutput = ['CR Number','Citations','Access Date','Total Score','Identification Score','Title','Authors','Year',
                         'Journal','Institution','Contact Author','PMID','DOI','Link','Languages','Medical Content Score',
                         'Keywords','Geographic Locations','Life Style','Medical History Taking-Family History',
                         'Social Work','Medical Histoy Taking-Medical/Surgical History','Signs and Symptoms','Comorbidities',
                         'Diagnostic Techniques and Procedures','Disease Diagnosis','Laboratory Values','Pathology',
                         'Pharmacological Therapy','Therapeutics','Patient Outcome Assesment',
                         'Relationship to Other Case Reports','Relationship with Clinical Trial','Crosslink with Database',
                         'Acknowledgements Score','Funding Source','Award Number','Disclosures','References',
#                         'Impact Factor',
                         'Age','Gender',
                         'Cancer','Nervous System Diseases','Cardiovascular Diseases',
                         'Musculoskeletal Diseases and Rheumatological Diseases','Digestive System Diseases',
                         'Obstetrical and Gynecological Diseases',
                         'Infectious Diseases','Respiratory Tract Diseases','Hematologic Diseases',
                         'Kidney Diseases and Urologic Diseases','Endocrine System Diseases',
                         'Oral and Maxillofacial Diseases','Ophthalmological Diseases','Otorhinolaryngologic Diseases',
                         'Skin Diseases','Rare Diseases','AllDiseaseSystems',
                         'Images','Graphs or Illustrations','Videos','Tables','Filename','Contributor']

df1 = pd.DataFrame(tmpList, columns=columnNamesOutput)
#print(df1.iloc[0,10:30])
df1.to_csv("AllCaseReports.csv", sep='\t', encoding='utf-8')

