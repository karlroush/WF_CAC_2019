# -*- coding: utf-8 -*-
"""
This file outputs the data from the initial LDA analysis

@author: kroush7
"""

from config import *
import csv

def LDA_output_test(subtopic_search, IDs):
#    print(IDs)
#    print(res_score)
    data=[['sub_topic','dataset_id']]
    i=0
    while i<len(subtopic_search):
        new_data=[subtopic_search[i], IDs[i]]
        data.append(new_data)
        i+=1
    file = open('../results/test_LDA_out.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)
