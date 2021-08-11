# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:47:38 2019

@author: kroush7
"""
from config import *

def LDA_title(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(texts) for texts in texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    
   #expiremental multithreading
#    lda_model = models.LdaMulticore(corpus, num_topics=8, id2word=dictionary, passes=200, workers=2)
#    for idx, topic in lda_model.print_topics(-1):
#        print('Topic: {} \nWords: {}'.format(idx, topic))
#    lda_model_tfidf = models.LdaMulticore(corpus_tfidf, num_topics=8, id2word=dictionary, passes=2, workers=2)
#    for idx, topic in lda_model_tfidf.print_topics(-1):
#        print('Topic: {} Word: {}'.format(idx, topic))
    
    #ldamodel = models.ldamodel.LdaModel(corpus_tfidf, num_topics=8, id2word = dictionary, passes=200)
#    for idx, topic in ldamodel.print_topics(-1):
#        print('Topic: {} \nWords: {}'.format(idx, topic))

    #print(ldamodel[corpus[1]])
# =============================================================================
#     res_topic_num=[]
#     res_score=[]
#     res_topic=[]
#     best_topic_num=[]
#     best_score=[]
#     best_topic=[]
#     for score in sorted(ldamodel[corpus[1]], key=lambda tup: -1*tup[1]):
#         print("\ncorpus: ")
#         print(corpus[0])
#         print("Score: {}\t \nTopic: {}".format(score, ldamodel.print_topic(0, 8)))
#         best_topic_num.append(score[0])
#         best_score.append(score[1])
#         best_topic.append(ldamodel.print_topic(0,8))
#     best_topic_num=best_topic_num[0]
#     best_score=best_score[0]
#     best_topic=best_topic[0]
#     res_topic_num.append(best_topic_num)  
#     res_score.append(best_score)
#     res_topic.append(best_topic)
#     return res_topic_num, res_score, res_topic
# =============================================================================

# =============================================================================
#      #print(ldamodel[corpus[0]])
#     res_topic_num=[]
#     res_score=[]
#     res_topic=[]
#  
#     for x in corpus:
#         best_topic_num=[]
#         best_score=[]
#         best_topic=[]
#         for score in sorted(ldamodel[x], key=lambda tup: -1*tup[1]):
#      #        print("\ncorpus: ")
#      #        print(corpus[0])
#      #        print("Score: {}\t \nTopic: {}".format(score, ldamodel.print_topic(0, 8)))
#              best_topic_num.append(score[0])
#              best_score.append(score[1])
#              best_topic.append(ldamodel.print_topic(0,8))
#         best_topic_num=best_topic_num[0]
#         best_score=best_score[0]
#         best_topic=best_topic[0]
#         res_topic_num.append(best_topic_num)  
#         res_score.append(best_score)
#         res_topic.append(best_topic)
#     print(res_topic_num)
#     print(res_score)
#     print(res_topic)
# 
# =============================================================================