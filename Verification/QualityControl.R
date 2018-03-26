

plan <- read.csv("AnnotationPlan.csv", header = TRUE, stringsAsFactors = FALSE)

ccr <- read.csv("ACCRs.tsv", header = TRUE, sep="\t", stringsAsFactors = FALSE)

ccr$CR.Number3 <- gsub("[^0-9]", "", ccr$CR.Number) 
ccr$CR.Number.Filename <- sapply(strsplit(ccr$Filename,"-"), function(x) gsub("[^0-9]","",x[1]))
library(dplyr)



############################## DUPLICATES #############################################
ccr %>% filter(PMID %in% ccr$PMID[duplicated(ccr$PMID)]) %>% arrange(desc(PMID)) %>% select(Filename, PMID, Access.Date)


############################## EMPTY TITLE ############################################
ccr %>% filter(Title=="nan") %>% select(Filename, PMID, Access.Date, Title)


############################## NAME AND CCR DIFFERENT #################################
ccr %>% filter(CR.Number3!=CR.Number.Filename) %>% arrange(desc(Filename)) %>% select(Filename,CR.Number, PMID, Access.Date)


############################## DUPLICATES CCR NUMBER #############################################
ccr %>% filter(CR.Number3 %in% ccr$CR.Number3[duplicated(ccr$CR.Number3)]) %>% arrange(desc(CR.Number3)) %>% select(Filename, PMID, CR.Number3, Access.Date)





#
############################## DIFFERENT THAN PLANNED #############################################
plan %>% filter(!plan$CCR.Number %in% as.numeric(ccr$CR.Number3) & Collector == "DL")
plan %>% filter(!plan$CCR.Number %in% as.numeric(ccr$CR.Number3) & !Collector %in% c("CQ","JZ","TC"))
plan %>% filter(!plan$CCR.Number %in% as.numeric(ccr$CR.Number3) & sort(desc(Collector)))




################################ CHECK IF PMID ALREADY DONE ###########################
ccr %>% filter(PMID == "1648845") %>% select(Filename, PMID, CR.Number3, Access.Date)




















##########################################
##########################################

aa <- as.data.frame(ccr %>% group_by(AllDiseaseSystems) %>% summarise(n=n()))
aa$AllDiseaseSystems

ccr$Filename[ccr$AllDiseaseSystems %in% "rare disease;transpositiongreatarteries"]
ccr$Filename[ccr$Contributor=="CF" & ccr$AllDiseaseSystems %in% c("rare disease;transpositiongreatarteries","rare disease; pyruvate dehydrogenase deficiency","rare disease; shone's complex","rare disease; tapvr","rare disease;hypoplastic left heart syndrome","rare disease;tetralogy of fallot" ,"rare disease, melorheostosis, bone dysplasia","neurological","nervous systm diseases; hematologic diseases","nervous systemnervous system dusease","nervous system diseases; endorine diseases","nervous system diseases; endorine system diseases","nervous sysmtem diseases","nan","musculoskeletal diseases hematologic diseases nervous system diseases","musculoskeletal diseases nervous system diseases","mitochondrial diseases; cardiovascular diseases; rare diseases","muscular diseases and rheumatological diseases; cardiovascular diseases","musculo & rheu diseases","musculo & rheu diseases;","musculo & rheu diseases; nervous system diseases","musculo & rheu diseases; nervous system diseases; cardiovascular diseases","kidney diseases and urologic diseasesl","kidney diseases and urologica diseases","kidney disease and urology diseases, rare disease" ,"hfref","hematological, nephrological","gi","endorcine diseases","endocrine system diseasses","digestive","cardiovascular diseasses","cardiovascular diseases; lung diseases; rare diseases; mitochondrial diseases; neurological diseases;","cancer;igestive system diseases; endocrine system diseases")]

## CFs done
# edit all those wrongly named disease systems

ccr$Filename[ccr$AllDiseaseSystems=="nan"]
# empty disease systems


bb <- ccr %>% filter(AllDiseaseSystems %in% c("rare disease;transpositiongreatarteries","rare disease; pyruvate dehydrogenase deficiency","rare disease; shone's complex","rare disease; tapvr","rare disease;hypoplastic left heart syndrome","rare disease;tetralogy of fallot" ,"rare disease, melorheostosis, bone dysplasia","neurological","nervous systm diseases; hematologic diseases","nervous systemnervous system dusease","nervous system diseases; endorine diseases","nervous system diseases; endorine system diseases","nervous sysmtem diseases","nan","musculoskeletal diseases hematologic diseases nervous system diseases","musculoskeletal diseases nervous system diseases","mitochondrial diseases; cardiovascular diseases; rare diseases","muscular diseases and rheumatological diseases; cardiovascular diseases","musculo & rheu diseases","musculo & rheu diseases;","musculo & rheu diseases; nervous system diseases","musculo & rheu diseases; nervous system diseases; cardiovascular diseases","kidney diseases and urologic diseasesl","kidney diseases and urologica diseases","kidney diseases and urological diseases","kidney disease and urology diseases, rare disease" ,"hfref","hematological, nephrological","gi","endorcine diseases","endocrine system diseasses","digestive","cardiovascular diseasses","cardiovascular diseases; lung diseases; rare diseases; mitochondrial diseases; neurological diseases;","cancer;igestive system diseases; endocrine system diseases")) %>% select(Filename,Contributor, AllDiseaseSystems,Rare.Diseases) %>% arrange(desc(Contributor))

bb <- ccr %>% filter(AllDiseaseSystems %in% c("hfref")) %>% select(Filename,Contributor, AllDiseaseSystems,Rare.Diseases) %>% arrange(desc(Contributor))



ccr %>% filter(CR.Number=="") %>% select(Filename)

