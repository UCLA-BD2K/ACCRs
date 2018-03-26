import sys
import io
import os
import re
from openpyxl import load_workbook
from word2number import w2n
import unicodecsv as csv
import pandas as pd
import xlrd
import numpy as np
import datetime

errors = []

def getFile(inputDirectoryPath, f):
    myX = pd.ExcelFile(inputDirectoryPath + f)
    file_base=f[0:-5].strip()
    contributor=file_base[-2:].upper().strip()

    if len(myX.sheet_names) > 1 and contributor == "DL":
        myDF = pd.read_excel(myX, sheetname=myX.sheet_names[len(myX.sheet_names)-1], header=None, parse_cols="A:E", encoding="utf-8")
    else:
        myDF = pd.read_excel(myX, sheetname=myX.sheet_names[0], header=None, parse_cols="A:E", encoding="utf-8")

    if contributor=="TC" or (contributor=="SM" and f[0]=="H"):
        myDF=myDF.drop(4).reset_index(drop=True)

    rowNames = ["cr_number","citation","access_date","score_total","score_identification","title","authors",
                "year","journal","institution","senior_author","pmid","doi","link","languages",
                "score_medicalcontent","keywords","demographics","geographic_location","lifestyle","family_history",
                "medical_background","medical_surgical_history","organ_system","symptoms_signs","comorbidities",
                "diagnositic_procedures","disease_diagnosis","laboratory_values","pathology","pharmacological_therapy",
                "therapeutic_intervention","outcome","images_videos","relationship_to_other_case_reports",
                "relationship_to_published_clinical_trials","crosslink_database","score_acknowledgements","funding_source",
                "award_number","disclosures_conflict_of_interest","references"]
    myDF = myDF.drop(myDF.index[[1,4,6,18,41]])
    myDF = myDF.reset_index(drop=True)
    myDF = myDF.loc[0:41,0:5]
    myDF['rowNames'] = rowNames
    myDF = myDF.set_index('rowNames')
    return myDF
    
    
    
def formatCell(cells, content=True):
    tmpValues = {}
    tmpValues["cellName"] = cells.name
    tmpValues["s1"] = cells[1]
    tmpValues["s2"] = cells[2]
    if content:
        tmpValues["r1"] = unicode(cells[3]).replace(u'\n',u' ').replace(u'\xa0',u' ').strip().lower()
        tmpValues["r2"] = unicode(cells[4]).replace(u'\n',u' ').replace(u'\xa0',u' ').strip().lower()
        if tmpValues["r1"] == u"nan":
            tmpValues["content"] = tmpValues["r2"]
        else:
            tmpValues["content"] = tmpValues["r1"]
    if cells.name == "journal":
        if len(cells) > 5:
            tmpValues["r3"] = unicode(cells[5]).replace(u'\n',u' ').replace(u'\xa0',u' ').strip().lower()
        else:
            tmpValues["r3"] = u'nan'
        tmpValues["r1"] = tmpValues["r1"].lower().replace(u'.',u'').replace(u'the journal',u'journal')
    if 'content' not in tmpValues:
        tmpValues["content"] = tmpValues["s1"]
    return tmpValues

def extractCells(myDF):
    results = []
    for index, elem in enumerate(myDF.index):
        if "score" in elem or elem in ["cr_number","citation","access_date"]:
            results.append(formatCell(myDF.loc[elem], False))
        else:
            results.append(formatCell(myDF.loc[elem]))
    return results


def getImpactFactor(journalString):
	impact_factors = {}
	journal_dict = {}
	not_present_journals = set()
	impact_error_num1 = 0
	impact_error_num2 = 0
	with open('./impact_dict.txt','r') as impact_js:
		for line in impact_js:
			line = line.split('\t')
			j = line[0].strip()
			i = line[1].strip()
			impact_factors[j] = i
	with open('./journal_dict.txt','r') as all_js:
		for line in all_js:
			line = line.split('\t')
			name = line[0].strip()
			correct = line[1].strip()
			journal_dict[name] = correct

	if journalString['content'] in journal_dict:
		journalString['content'] = journal_dict[journalString['content']]
		impact = impact_factors[journalString['content']]
	elif journalString['r3'] == u"nan":
		impact = journalString['r3']
		e = u'ERROR: ' + journalString['content'] + u' not listed in impact factor table and not in excel sheet'
		errors.append(e)
		not_present_journals.add(journalString['content'])
	else:
		impact = journalString['r3']
		e = u'WARNING ' + journalString['content'] + u' not listed in impact factor table'
		errors.append(e)
		not_present_journals.add(journalString['content'])
	return impact

def verifyPMID(pmidString, f):
    if pmidString['content'] not in f:
        print u'ERROR! PMID does not match file name.  PMID is ' + pmidString['content'] + u' and file name is ' + f
        errors.append(u'ERROR: PMID does not match file name. PMID is ' + pmidString['content'] + u' and file name is ' + f)

        

def getAge(ageString):
    age_string = re.sub(ur'\< 18 yo','less than 18 years old', ageString['content'].encode('utf-8').lower())##
    yeardate = re.findall(ur'[1-2][0-9]{3}',age_string)
    years = re.findall(ur'(\d+(?:\.\d+)?)([^\w\d]+)(year|yr|yo|y\/o)',age_string)
    more_years = re.findall(ur'(?:aged?|age of)[^\w\d]+(\d+(?:\.\d+)?)',age_string)#AGE OF ONE?
    writ_years = re.findall(ur'((?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|one hundred|one hundred and)(?:[^\w\d]+)(?:(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)(?:[^\w\d]+))?)(year|yr|yo|y\/o)',age_string)
    decades = re.findall(ur'twenties|thirties|forties|fifties|sixties|seventies|eighties|nineties|20s|30s|40s|50s|60s|70s|80s|90s|20\'s|30\'s|40\'s|50\'s|60\'s|70\'s|80\'s|90\'s',age_string)#20's-->and switch all bad ' to '
    months = re.findall(ur'(\d+(?:\.\d+)?)([^\w\d]+)(month)',age_string)
    days = re.findall(ur'(\d+(?:\.\d+)?)([^\w\d]+)(day)',age_string)
    weeks = re.findall(ur'(\d+(?:\.\d+)?)([^\w\d]+)(week|wk)(?! premature)',age_string)
    newborn = re.findall(ur'(?:newborn|infant|neonate)',age_string)
    decade_conv = {'twenties':25, '20s':25, '20\'s':25, 'thirties':35, '30s':35, '30\'s':35, 'fourties':45, '40s':45,
                   '40\'s':45, '50s':55, '50\'s':55, 'fifties':55, 'sixties':65, '60s':65, '60\'s':65, 'seventies':75,
                   '70s':75, '70\'s':75, 'eighties':85, '80s':85, '80\'s':85, 'nineties':95, '90s':95, '90\'s':95}
    if len(yeardate) >= 1:
        age = int(datetime.date.today().year) - int(yeardate[0])
    elif len(years) >= 1:
        age = years[0][0]
    elif len(more_years) >= 1:
        age = more_years[0]
    elif len(months) >= 1:
        age = float(months[0][0]) / 12.0
    elif len(writ_years) >= 1:
        age = w2n.word_to_num(str(writ_years[0][0]))
    elif len(decades) >= 1:
        age = decade_conv[decades[0]]
    elif len(days) >= 1:
        month = 1
        if float(days[0][0])/30.0 > month:
            month = float(days[0][0]) / 30.0
        age = month / 12.0
    elif len(weeks) >= 1:
        month = 1
        if float(weeks[0][0])/4.0 > month :
            month = float(weeks[0][0]) / 4.0
        age = month / 12.0
    elif len(newborn) >= 1:
        age = 1 / 12.0
    else:
        age = u'NA'
    age = unicode(age) ##
    return age



def getGender(genderString, f):
    gender_string = genderString['content'].encode('utf-8').lower() ##
    gender_string = re.sub(ur'woman|women|girl|lady|femal|sister', 'female', gender_string)
    gender_string = re.sub(ur'(?<!(?:wo|hu))man|(?<!wo)men|boy', 'male', gender_string)
    genders = set(re.findall(ur'female|male', gender_string, re.I))
    g2 = set(re.findall(ur'female|male', gender_string, re.I))

    #####_PARSE_GENDER_########
    if len(genders) == 1:
        gender = unicode(genders.pop().lower())
    elif len(genders) == 2:
        if len(g2) == 1:
            gender = unicode(g2.pop().lower())
            e = u'Warning: Both male and female reported as gender. There should only be one gender, because we should be using only the first case report. MeSH terms columns has one gender, so using that one, but this could be wrong.'
            errors.append(e)
            print(e + u" " + f)
        else:
            gender = u'male & female'
            e = u'Warning: Both male and female reported as gender. There should only be one gender, because we should be using only the first case report. MeSH terms columns has one gender, so using that one, but this could be wrong.'
            errors.append(e)
    elif len(genders) == 0:
        if len(g2) == 0:
            gender = u"NA"
        elif len(g2) == 1:
            gender = unicode(g2.pop().lower())
        elif len(g2) == 2:
            gender = u'male & female'
            e = u'Warning: Both male and female reported as gender. There should only be one gender, because we should be using only the first case report. MeSH terms columns has one gender, so using that one, but this could be wrong.'
            errors.append(e)
        else:
            print(g2)
            g_str = u""
            for g in g2:
                g_str = g_str + g + u"_"
            e = u"Error: Length of gender string greater than two: " + g_str
            errors.append(e)
            print(e + u" in file " + f)
    else:
        e = u"Error: Length of gender string greater than two"
        errors.append(e)
        print(e + u" in file " + f)
    return gender



def getOrganSystem(organString):
    organSystems = [['cancer'], 
                ['nervous', 'neurologic', 'neurological'],
                ['cardio'],
                ['musculoskeletal', 'rheumatologic'],
                ['digestive', 'gastrointestinal'],
                ['obstetrical', 'gynecological'], #'gi'?
                ['infectious'],
                ['respiratory'],
                ['hematologic', 'blood'],
                ['kidney', 'urologic', 'urinary', 'nephrologic'],
                ['endocrin', 'endorine'],
                ['oral', 'maxillofacial'],
                ['ophthalm', 'eye'],
                ['otorhinolaryngologic'],
                ['skin', 'dermatological'],
                ['rare']
               ]

    if organString['content'] == u"nan":
        OrganSystem = [u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA',u'NA']
        e = u"Error, no disease system listed"
        errors.append(e)
    else:
        text = re.split(',|;',organString['content'].encode('utf-8').lower()) ###
        error = u""
        if len(text) <= 0:
            OrganSystem=['ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR',
                         'ERROR','ERROR','ERROR','ERROR','ERROR','ERROR']##
        else:
            valuesOrgan = []
            for s in text:
                valuesOrgan.append(np.array([any(word in s for word in elem) for index, elem in enumerate(organSystems)]))
            OrganSystem = [sum(x) for x in zip(*valuesOrgan)]
    OrganSystem.extend([organString['content']])
    return OrganSystem



def getDatabase(databaseString, f):
    crosslinkWithDatabase = u"nan"
    if databaseString['content'] != u"nan":
        nums = re.findall(ur'(?:^\d+ | \d+)', databaseString['content'].encode('utf-8')) #######handle unicode!!!!!
        my_sum = 0
        if len(nums) >0:
            for n in nums:
                my_sum = my_sum + int(n.strip())
                crosslinkWithDatabase = unicode(my_sum)
        else:
            urls = re.findall(ur'https:\S*', databaseString['content'].encode('utf-8'))
            if len(urls) > 0:
                crosslinkWithDatabase = unicode(len(urls))#+'*'
                errors.append(u"WARNING: Crosslinks in wrong format, computing answer assuming only 1 crosslink per link")
            else:
                crosslinkWithDatabase = u"ERROR"
                e = u"ERROR: Parsing error in crosslink with database row"
                errors.append(e)
                print(e + u" in file " + f)
    return crosslinkWithDatabase

def getImagesVideos(imageVideoString, f):
    media = [0,0,0,0]
    if imageVideoString['content'] == u"nan":
        e = u"Error: Cannot parse Images or Videos because not listed"
        errors.append(e)
    else:
        image_nums = re.findall(ur'\d+(?<! Figure)', imageVideoString['content'].encode('utf-8')) ####handle unicode!
        if len(image_nums) == 4:
            media = image_nums
        elif len(image_nums) == 2:
            media = [image_nums[0],0,image_nums[1],0]
            e = "Warning: Missing number of illustrations/graphs and number of tables"
            errors.append(e)
        elif len(image_nums) == 1:
            media = [image_nums[0],0,0,0]
            e = "Warning: Missing numbers of illustrations/graphs, videos, and tables"
            errors.append(e)
        else:
            e = u"ERROR: IMAGE NUMBERS IN WRONG FORMAT"
            errors.append(e)
            print(e + u": " + imageVideoString['content'] + u" (in file " + unicode(f) + u")")
    return media


def getReferences(referencesString, f):
    references = u'NA'
    if referencesString['content'] != u"nan":
        ref_nums = re.findall(ur'\d+', referencesString['content'].encode('utf-8')) #####handle unicode
        if len(ref_nums) >= 1:
            references = ref_nums[0]
            if len(ref_nums) > 1:
                e = u'Warning, references cell has multiple numbers. Taking first one.'
                errors.append(e)
#                print(e + u" In file " + unicode(f))
        elif len(ref_nums) == 0:
            references == u"ERROR"
            e = u"ERROR: references in wrong format"
            errors.append(e)
            print(e + u": " + referencesString['content'] + u" (in file " + unicode(f) + ")")
    return references

def getDataFile(inputDirectoryPath, f):
	myDF = getFile(inputDirectoryPath, f)
	fileCells = extractCells(myDF)

	theList = [x["content"] for x in fileCells]
	theList.extend([getReferences(formatCell(myDF.loc['references']), f)])
#	theList.extend([getImpactFactor(formatCell(myDF.loc['journal']))])
	theList.extend([getAge(formatCell(myDF.loc['demographics']))])
	theList.extend([getGender(formatCell(myDF.loc['demographics']), f)])
	theList.extend(getOrganSystem(formatCell(myDF.loc['organ_system'])))
	theList.extend(getImagesVideos(formatCell(myDF.loc['images_videos']), f))
	theList.extend([f])

	file_base=f[0:-5].strip()
	contributor=file_base[-2:].upper().strip()

	theList.extend([contributor])

	theList = [v for i, v in enumerate(theList) if i not in {17,23,33,41}]
	return theList
