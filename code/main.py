# -*- coding: utf-8 -*-
"""
This is the main file where everything is run from

@author: kroush
"""

from config import *
from csvRead import tsvRead 
from user_comm import user_comm
from LDA_initial import LDA_title
from LDA_initial2 import LDA_desc
from LDA_initial_out import LDA_output
from LDA_novel_out import LDA_output_novel
from method_subTopicReq import tags
from id_print import id_print

from test_csvRead import tsvRead_test
from test_LDA_out import LDA_output_test

def main():
    plt.close("all") 
# =============================================================================
#     READ THE RAW DATA
# =============================================================================
    #intialize raw data dump
    print("\nParsing raw data...")
    start_time_n=time.time()
    filename='../a391d853147b-NASA_DataSets_Scrub.tsv' #data location
    
    filename2='../1_1003.tsv' #data location
    filename3='../1004_2003.tsv' #data location
    filename4='../2005_4007.tsv' #data location
    filename5='../8k.tsv' #data location
    
    search, raw_titles, raw_descriptions, IDs, title_tokens, title_tokens_all, desc_tokens, desc_tokens_all= tsvRead(filename)
#    search, raw_titles, raw_descriptions, IDs= tsvRead_test(filename5) #speed testing
    print("--- %s seconds for parsing ---" % (time.time() - start_time_n))

    #I ran this in blocks on file subsets since my computer is bit slow
    #i.e. I uncommented line 72 and ran main() with different file names on line 31
    print("\nBeginning sub-topic generation. Warning this may take awhile...") #novel approach for subtopics
    start_time_n=start_time
    count=0
    subtopic_search=[]
    total=len(search)
    for item in search:
        count+=1
#        if count>2: uncomment the following lines for testing
#            pass
#        else:
        subtopic_n= tags(item) #you'll need to indent this and the next for testing
        subtopic_search.append(subtopic_n)
        print("Current subtopic= %s out of %s" % (count, total))
    print("--- %s seconds for search ---" % (time.time() - start_time_n))
    
    
# =============================================================================
#     Initial Analysis
# =============================================================================
    
    fdist_title = FreqDist(title_tokens_all) #frequency distribution of words
    fdist_desc = FreqDist(desc_tokens_all)
    print(fdist_title.most_common(10)) #this shows the most common words (number specified)
    print(fdist_desc.most_common(10))
    user_comm(fdist_title,fdist_desc) #graphs  
    
    
# =============================================================================
#     Output for the initial LDA model
# =============================================================================
    print("\nGenerating model...")
    start_time_n=time.time()
    res_topic_num, res_score, res_topic=LDA_title(title_tokens)
    res_subtopic_num, res_subscore, res_subtopic= LDA_desc(desc_tokens)
    print("--- %s seconds for output ---" % (time.time() - start_time_n))
    
    print("\nOutputing data...")
    start_time_n=time.time()
    id_print(IDs) #validate ID sequence
#    LDA_output_test(subtopic_search, IDs) #speed testing
    LDA_output(res_topic_num, res_subtopic_num, IDs, res_score, res_subscore)
#    LDA_output_novel(res_topic_num, res_subtopic_num, IDs, res_score, res_subscore, subtopic_search) #novel approach
    print("--- %s seconds for output ---" % (time.time() - start_time_n))
    
start_time = time.time() #to time how long it takes to run
main()
print("\n--- %s seconds overall ---" % (time.time() - start_time))