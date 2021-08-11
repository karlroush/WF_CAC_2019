# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:07:05 2019

@author: kroush7
"""

# importing the requests library 
import requests 
from bs4 import BeautifulSoup
base='https://catalog.data.gov/dataset/'
data_set='3d-flash-lidar-all-weather-safety-phase-i'
url=base+data_set

#open with GET method 
resp=requests.get(url) 

#http_respone 200 means OK status 
if resp.status_code==200: 
    print("Successfully opened the web page") 
    soup=BeautifulSoup(resp.text,'html.parser')  
    tags=soup.find_all("a",{"class":"tag"})
    a=len(tags)
    for b in tags:
        print(b.get_text())
    print(a)
#    for x in tags
#        print(soup.find_all("a",{"class":"tag"}))
#        print(soup.find_all("a",{"class":"tag"})[0].get_text())
else: 
    print("Error") 
