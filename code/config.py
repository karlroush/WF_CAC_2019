# -*- coding: utf-8 -*-
"""
This is the configuration file for all the scripts
It contains the required packages

@author: kroush
"""

import csv
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import time
import matplotlib.pyplot as plt
from gensim import corpora, models
import requests 
from bs4 import BeautifulSoup

# =============================================================================
# #to show plots not inline use
# #   %matplotlib qt
# # inline is 
# #   %matplotlib inline
# =============================================================================
