# -*- coding: utf-8 -*-
"""
This file reads the raw data from the provided .tsv for testing
It also tokenizes the titles & descriptions, then reduces them to word stems

@author: kroush
"""
from config import *
import csv

def tsvRead_test(filename):   
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
        temp=temp.replace(')','')
        temp=temp.replace('(','')
        temp=temp.replace('&','') #
        temp=temp.replace(':','') #
        temp=temp.replace('\'','') #
        temp=temp.replace('+','') #
        temp=temp.replace('>','') #
        temp=temp.replace('<','') #
        temp=temp.replace('/','-')
        temp=temp.replace('.','-')
        temp=temp.lower()
        temp=temp.replace(" ", "-")
        temp=temp.replace("---", "-")
        temp=temp.replace("--", "-")
        temp=temp[0:90]
        search.append(temp)
    #print(search)  
    return search, raw_titles, raw_descriptions, IDs