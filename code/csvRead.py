# -*- coding: utf-8 -*-
"""
This file reads the raw data from the provided .tsv
It also tokenizes the titles & descriptions, then reduces them to word stems

@author: kroush
"""
from config import *
import csv

def tsvRead(filename):   
    raw_titles=[]
    issued=[]
    modified=[]
    raw_descriptions=[]
    IDs=[]
    search=[]
# =============================================================================
#     Read the data file
# =============================================================================
    count=0
    with open(filename,encoding="utf-8") as tsvfile:
          reader = csv.DictReader(tsvfile, dialect='excel-tab')
          for row in reader:    #append each item to appropriate data dump
              raw_titles.append(row['title'])
              issued.append(row['issued'])
              modified.append(row['modified'])
              raw_descriptions.append(row['description'])
              IDs.append(row['id'])
    for item in raw_titles:
        temp=item.replace(',','')
        temp=temp.strip()
        temp=temp.replace(')','')
        temp=temp.replace('\\','')
        temp=temp.replace('(','')
        temp=temp.replace('&','') #
        temp=temp.replace(':','') #
        temp=temp.replace('’','') #
        temp=temp.replace('\'','') #
        temp=temp.replace('+','') #
        temp=temp.replace('>','') #
        temp=temp.replace('<','') #
        temp=temp.replace('/','-')
        temp=temp.replace('.','-')
        temp=temp.replace('_','-')
        temp=temp.lower()
        temp=temp.replace(" ", "-")
        temp=temp.replace("----", "-")
        temp=temp.replace("---", "-")
        temp=temp.replace("--", "-")
        temp=temp[0:90]
        search.append(temp)
    #print(search)
        
# =============================================================================
#     TOKENIZE THE TITLES FOR ANALYSIS
# =============================================================================
    title_tokens=[]
    title_tokens_all=[]
    for w in raw_titles:
        #tokenize titles 
        tokens=word_tokenize(w)
        tokens=[w for w in tokens if re.search('^[^(?!Phase.I.)]', w)] #remove phase and commas
        tokens=[w for w in tokens if re.search('^[^().,/&#;\[\]:]', w)] #remove assorted punctuation
        tokens=[w for w in tokens if re.search('^(?!.*[x]{2,})', w)] #remove instances of multiple x's
        tokens=[w for w in tokens if re.search('^[^(V...)]', w)] #remove V.xx
        tokens=[w for w in tokens if re.search('^(?![0-9])', w)] #remove [0-9].[0-9]

        #remove stop words
        en_stop = stopwords.words('english')
        en_stop.append('the')
        stopped_tokens = [i for i in tokens if not i in en_stop]
        #reduce tokens to stems
        p_stemmer = PorterStemmer()
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        title_tokens.append(stemmed_tokens)
        for n in stemmed_tokens:
            title_tokens_all.append(n)
       
# =============================================================================
#     TOKENIZE THE DESCRIPTIONS FOR ANALYSIS
# =============================================================================
    desc_tokens=[]
    desc_tokens_all=[]
    for w in raw_descriptions:
        #tokenize titles 
        tokens2=word_tokenize(w)
        tokens2=[w for w in tokens2 if re.search('^[^(?!Phase.I.)]', w)] #remove phase and commas
        tokens2=[w for w in tokens2 if re.search('^[^().,/&#;\[\]]', w)] #remove assorted punctuation
        tokens2=[w for w in tokens2 if re.search('^(?!.*[x]{2,})', w)] #remove instances of multiple x's
        tokens2=[w for w in tokens2 if re.search('^[^(V...)]', w)] #remove V.xx
        tokens2=[w for w in tokens2 if re.search('^(?![0-9])', w)] #remove [0-9].[0-9]
        tokens2=[w for w in tokens2 if re.search("^(?![\', \'])", w)]
        tokens2=[w for w in tokens2 if re.search('^(?!not applicable)^(?!N/A)', w)] #remove N/A's

        #remove stop words
        stopped_tokens2 = [i for i in tokens2 if not i in en_stop]
        #reduce tokens to stems
        stemmed_tokens2 = [p_stemmer.stem(i) for i in stopped_tokens2]
        desc_tokens.append(stemmed_tokens2)  
        for n in stemmed_tokens2:
            desc_tokens_all.append(n)      
    
    return search, raw_titles, raw_descriptions, IDs, title_tokens, title_tokens_all, desc_tokens, desc_tokens_all