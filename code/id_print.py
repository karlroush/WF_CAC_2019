# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:35:11 2019

@author: Karl Roush
"""
from config import *
import csv

def id_print(IDs):
#    print(IDs)
#    print(res_score)
    data=[['IDs']]
    i=0
    while i<len(IDs):
        new_data=[IDs[i]]
        data.append(new_data)
        i+=1
    file = open('../results/ID.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)
