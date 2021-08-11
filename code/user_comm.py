# -*- coding: utf-8 -*-
"""
This script outputs visualizations of the data for the end user

@author: kroush7
"""
from config import *

def user_comm(fdist_title,fdist_desc):
    plt.figure()
    plt.title("Titles: Cumulative Word Distribution (Top 50)")
    fdist_title.plot(50, cumulative=True)
    
    plt.figure()
    plt.title("Descriptions: Cumulative Word Distribution (Top 50)")
    fdist_desc.plot(50, cumulative=True)
