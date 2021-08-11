# -*- coding: utf-8 -*-
"""
This file makes requests to 

@author: kroush7
"""

from config import *

def tags(data_set):
    subtopics=[]
    base='https://catalog.data.gov/dataset/'
    #data_set='3d-flash-lidar-all-weather-safety-phase-i'
    url=base+data_set
    
    #open with GET method 
    resp=requests.get(url) 
    
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        #print("Successfully opened the web page") 
        soup=BeautifulSoup(resp.text,'html.parser')  
        tags=soup.find_all("a",{"class":"tag"})
        a=len(tags)
        for b in tags:
            subtopics.append(b.get_text())
            #print(b.get_text())
    else: 
        print("Error in parsing, check delimeters")
        subtopics.append('Error')
        print(data_set)
    #print(subtopics)
    
    return subtopics