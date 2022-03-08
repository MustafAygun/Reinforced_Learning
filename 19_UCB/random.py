# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:54:22 2021

@author: Mustafa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("Ads_CTR_Optimisation.csv")

import random

N=10000
d=10
secilenler=[]
toplam=0
for n in range(0,N):
    rnd= random.randrange(d)
    secilenler.append(rnd)
    odul= veriler.values[n,rnd]
    toplam = toplam + odul
    
plt.hist(secilenler)
plt.show()