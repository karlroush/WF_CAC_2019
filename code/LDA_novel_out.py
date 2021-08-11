# -*- coding: utf-8 -*-
"""
This file outputs the data from the novel LDA analysis

@author: kroush7
"""

from config import *
import csv

def LDA_output_novel(res_topic_num, res_subtopic_num, IDs, res_score, res_subscore, subtopic_search):
#    print(IDs)
#    print(res_score)
    data=[['topic', 'sub_topic','dataset_id', 'topic_confidence', 'sub_topic_confidence']]
    i=0
    while i<len(res_topic_num):
        new_data=[res_topic_num[i],subtopic_search[i], IDs[i], res_score[i], res_subscore[i]]
        data.append(new_data)
        i+=1
    file = open('../results/novel_LDA_out.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)
