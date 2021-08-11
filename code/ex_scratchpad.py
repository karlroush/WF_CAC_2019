# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:31:49 2019

@author: kroush7
"""
import numpy as np
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#from nltk.book import *


#need to tokenize based on words I care about (and ditch extraneous)
s1= "Novel Hybrid Propulsion System for Sample Return Missions, Phase III Power"
s2="The xxxxxx xxxxxx Separator (xxxxxxS) is an innovative method to beneficiate soil prior to in-situ resource utilization (ISRU). The xxxxxxS can improve ISRU oxygen yield by boosting the concentration of ilmenite or other iron-oxide bearing materials found in lunar soils. This can substantially reduce hydrogen reduction reactor size and drastically decrease the power input required for soil heating. xxxxxxS particle size separations can be performed to de-dust regolith and to improve ISRU reactor flow dynamics. xxxxxxS mineral separations can be used to alter the sintering characteristics of lunar soil. The xxxxxxS can also be used to separate and concentrate lunar minerals useful for manufacture of structural materials, glass, and chemicals. The xxxxxxS integrates an initial centrifugal particle size separation with magnetic, gravity, and electrostatic separations. The xxxxxxS centrifugal separation method overcomes the reduced efficiency of conventional particle sieving in reduced gravity. The xxxxxxS hardware design integrates many individual unit operations to reduce system mass and power requirements. The xxxxxxS is applicable to ISRU feed processing as well as robotic prospecting to characterize soils over wide regions on the xxxxxx. The xxxxxxS is scalable and is amenable to testing and development in vacuum and reduced gravity."
print(s1)
tokens=word_tokenize(s1)
print(tokens)
tokens=[w for w in tokens if re.search('^[^Phase,I]', w)] #remove phase and commas
print(tokens)

'''
tokens2=word_tokenize(s2)
print(tokens2)
tokens2=[w for w in tokens2 if re.search('^[^x().,]', w)] #remove the x's and assorted punctuation
print(tokens2)

fdist1 = FreqDist(tokens2)
'''

'''
# remove stop words & stemming
en_stop = stopwords.words('english')
stopped_tokens = [i for i in tokens if not i in en_stop]
print(stopped_tokens)
p_stemmer = PorterStemmer()
stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
print(stemmed_tokens)
'''