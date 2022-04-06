import glob
import re
import os
import nltk
#nltk.download('omw-1.4')
#nltk.download('punkt')
#nltk.download('wordnet')
from nltk.corpus import wordnet
from transformers import pipeline
from transformers import AutoModel
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import TokenClassificationPipeline
from transformers import BertTokenizer


def name_redaction(lines):

    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", use_fast=True)
    nlp = TokenClassificationPipeline(model=model, tokenizer=tokenizer, grouped_entities=True)
    output = nlp(lines)
    name_count=0
    for i in output:
        if i['entity_group'] == 'ORG' or i['entity_group'] == 'PER':
            name_count=name_count+1
            for j in range(i['start'], i['end']):
                lines = lines[:j] + "█" + lines[j+1:]

    #print(name_count)
    #print(lines)

    return lines, name_count

####################################################################################


def gender_redaction(lines):

    gender_list=[' father ',' mother ',' she ',' her ',' he ',' his ',' woman ',' women ',' men ',' man ',' female ',' male ',' him ',' wife ',' husband ',' Father ',' Mother ',' She ',' Her ',' He ',' His ',' Woman ',' Women ',' Men ',' Man ',' Female ',' Male ',' Him ',' Wife ',' Husband ']
    gender_count1=[]
    for k in gender_list:
        if k in lines:
            x= '█' * len(k)
            #start=str(lines.find(k))
             #print(start)
            count=lines.count(k)
            #print(count)
            gender_count1.append(count)
            lines=lines.replace(k,x)
    gender_count=sum(gender_count1)
    #print(gender_count)
    #print(lines)
    #print(gender_count)
    return lines,gender_count



#######################################################################################################

def date_redaction(lines):


    date_match1=re.findall(r'\d{1,2}\s+[A-Za-z]*\s+\d{2,4}',lines)
    #print(date_match1)
    for l in date_match1:
        if l in lines:
            x= "█" * len(l)
            lines=lines.replace(l,x)
    #print(lines)
    date_count1=len(date_match1)

    date_match2=re.findall(r'[0-9]{1,2}[/][0-9]{1,2}[/][0-9]{4}',lines)
    #print(date_match2)
    for i in date_match2:
        if i in lines:
            x= "█" * len(i)
            lines=lines.replace(i,x)
    #print(lines)
    date_count2=len(date_match2)

    date_match3=re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{0,1}\d{2,4}',lines)
    #print(date_match3)
    for m in date_match3:
        if m in lines:
            x= "█" * len(m)
            lines=lines.replace(m,x)
    #print(lines)
    date_count3=len(date_match3)
    date_count=date_count1+date_count2+date_count3
    return lines,date_count






###########################################################################################################

def phonenumbers_redaction(lines):


    phone_match1=re.findall(r'[+]?\d{1,3}[-]\d{3}[-]\d{3}[-]\d{4}',lines)
    for i in phone_match1:
        if i in lines:
            x= "█" * len(i)
            lines=lines.replace(i,x)
    #print(lines)
    phone_count1=len(phone_match1)



    phone_match2=re.findall(r'[+]{1}\d{1,3}\s{0,1}\d{3}\s{0,1}\d{3}\s{0,1}\d{4}',lines)
    for i in phone_match2:
        if i in lines:
            x= "█" * len(i)
            lines=lines.replace(i,x)
    #print(lines)
    phone_count2=len(phone_match2)
    phone_count=phone_count1+phone_count2
    return lines,phone_count


######################################################################################################

def address_redaction(lines):

    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", use_fast=True)
    nlp = TokenClassificationPipeline(model=model, tokenizer=tokenizer, grouped_entities=True)
    #print(lines)
    address_count1=0
    location=nlp(lines)
    for i in location:
        if i['entity_group'] == 'LOC':
            address_count1=address_count1+1
            for j in range(i['start'], i['end']):
                lines = lines[:j] + "█" + lines[j+1:]
    #print(lines)

    address_match1=re.findall(r'\d{1,}\s(?:East|West|North|South|E|W|N|S|NE|NW|SE|SW)\s?\w{1,}',lines)
    #print(address_match)
    for i in address_match1:
        if i in lines:
            x= "█" * len(i)
            lines=lines.replace(i,x)
    #print(lines)
    address_count2=len(address_match1)
    address_count=address_count1+address_count2
    #print(address_count)

    return lines,address_count

def concept_redaction(lines,word):


    concept_words=[]
    words=[]
    word_list = []
    x=wordnet.synsets(word)
    #print(x)
    for i in x:
        for j in i.lemmas():
            concept_words.append(j.name())
    #print(words)
    sentences=nltk.sent_tokenize(lines)
    #print(sentences)
    for i in sentences:
        tok_words=nltk.word_tokenize(i)
        for j in tok_words:
            if j in concept_words:
                n = "█" * len(i)
                lines = lines.replace(i,n)
                break;
#    print(lines)
    return lines
###########################################################################################################3


def output(lines,i,foldername):
#output

    d=os.getcwd()
    #print(d)
    import ntpath
    path1= ntpath.basename(i)
    path=path1[:-4]
    #print(path)
    #print(ntpath.basename(lis[9]))
    #dir="Output_files"
    path2 = os.path.join(d+'/', foldername)
    if not os.path.exists(path2):
        os.makedirs(path2)
    completepath=os.path.join(path2,path+'.redacted')
    with open(completepath,'w', encoding='utf-8') as ofile:
        ofile.writelines(lines)
        ofile.close()
    return path



def stats_files(stats_list,foldername):


    cwd_dir = os.getcwd()
#    print(cwd_dir)
    #folder_name="stats"
#    file_name="stder"
    path = os.path.join(cwd_dir + '/', foldername)
    if not os.path.exists(path):
        os.makedirs(path)
    filename=foldername+'.txt'
    with open(os.path.join(path+'/',filename),'a',encoding='UTF-8') as ofile:
        for key, value in stats_list.items():
            items_list = [str(item) for item in value]
            stats_string = ' '.join(items_list)
            ofile.write(str(key))
            ofile.write(str(stats_string))
        ofile.close()




