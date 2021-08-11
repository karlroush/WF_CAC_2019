# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 06:37:53 2019

@author: kroush7
"""

import csv
import config
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def tsvRead(filename):   
    raw_titles=[]
    issued=[]
    modified=[]
    raw_decriptions=[]
    IDs=[]
    
    with open(filename,encoding="utf-8") as tsvfile:
          reader = csv.DictReader(tsvfile, dialect='excel-tab')
          for row in reader:    #append each item to appropriate data dump
              #rawData.append(row)
              raw_titles.append(row['title'])
              issued.append(row['issued'])
              modified.append(row['modified'])
              raw_decriptions.append(row['description'])
              IDs.append(row['id'])
    
    ###### TOKENIZE THE TITLES FOR ANALYSIS
    title_tokens_all=[]
    for w in raw_titles:
        #tokenize titles 
        tokens=word_tokenize(w)
        tokens=[w for w in tokens if re.search('^[^(Phase),I]', w)] #remove phase and commas
        tokens=[w for w in tokens if re.search('^[^x().,/]', w)] #remove the x's and assorted punctuation
        tokens=[w for w in tokens if re.search('^[^(V...)]', w)] #remove V.xx
        tokens=[w for w in tokens if re.search('^(?![0-9])', w)] #remove [0-9].[0-9]
        
        #remove stop words
        en_stop = stopwords.words('english')
        stopped_tokens = [i for i in tokens if not i in en_stop]
        #reduce tokens to stems
        p_stemmer = PorterStemmer()
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        for n in stemmed_tokens:
            title_tokens_all.append(n)
       
    ###### TOKENIZE THE DESCRIPTIONS FOR ANALYSIS
    desc_tokens_all=[]
    for w in raw_decriptions:
        #tokenize titles 
        tokens2=word_tokenize(w)
        tokens2=[w for w in tokens2 if re.search('^[^(Phase)]', w)] #remove phase and commas
        tokens2=[w for w in tokens2 if re.search('^[^,]', w)] #remove phase and commas
        tokens2=[w for w in tokens2 if re.search('^[^x().,/]', w)] #remove the x's and assorted punctuation
        tokens2=[w for w in tokens2 if re.search('^[^(V...)]', w)] #remove V.xx
        tokens2=[w for w in tokens2 if re.search('^(?![0-9])', w)] #remove [0-9].[0-9]
        
        #remove stop words
        en_stop = stopwords.words('english')
        stopped_tokens2 = [i for i in tokens2 if not i in en_stop]
        #reduce tokens to stems
        p_stemmer = PorterStemmer()
        stemmed_tokens2 = [p_stemmer.stem(i) for i in stopped_tokens2]
        for n in stemmed_tokens2:
            desc_tokens_all.append(n)      
    
    return raw_titles, raw_decriptions, IDs, title_tokens_all, desc_tokens_all
#print('done')