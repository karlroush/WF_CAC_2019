# -*- coding: utf-8 -*-
"""
This file preforms an initial LDA analysis on the desc of the data

@author: kroush
"""
from config import *

def LDA_desc(desc_tokens):
    dictionary = corpora.Dictionary(desc_tokens)
    corpus = [dictionary.doc2bow(desc_tokens) for desc_tokens in desc_tokens]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    
    #construct the initial LDA model based on the titles
    ldamodel = models.ldamodel.LdaModel(corpus_tfidf, num_topics=3, id2word = dictionary, passes=5)
    
    outputmodel= ldamodel.print_topics(-1)
    #print(outputmodel)
    file = open('../results/initial_LDA_out_subtopicLabels.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerows(outputmodel)

#    for idx, topic in ldamodel.print_topics(-1):
#        print(idx)
#        print(topic)
#        print('Topic: {} \nWords: {}'.format(idx, topic))
        
    #this pulls the best topic number, its "equation", and a confidence value
    res_subtopic_num=[] #topic number
    res_subscore=[] #confidence value
    res_subtopic=[] #topic "equation"
    for x in corpus:
        best_topic_num=[]
        best_score=[]
        best_topic=[]
        for score in sorted(ldamodel[x], key=lambda tup: -1*tup[1]):
     #        print("\ncorpus: ")
     #        print(corpus[0])
     #        print("Score: {}\t \nTopic: {}".format(score, ldamodel.print_topic(0, 8)))
             best_topic_num.append(score[0])
             best_score.append(score[1])
             best_topic.append(ldamodel.print_topic(0,8))
        best_topic_num=best_topic_num[0]
        best_score=best_score[0]
        best_topic=best_topic[0]
        res_subtopic_num.append(best_topic_num)  
        res_subscore.append(best_score)
        res_subtopic.append(best_topic)
#    print(res_topic_num)
#    print(res_score)
#    print(res_topic)
    return res_subtopic_num, res_subscore, res_subtopic