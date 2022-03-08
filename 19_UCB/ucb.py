# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:54:22 2021

@author: Mustafa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("Ads_CTR_Optimisation.csv")

#random selection

"""
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
plt.show()"""

#ucb selection

import random

N=10000 #10000 tiklama
d=10 #toplam 10 ilan var
#Ri(n)

toplam=0

secilenler=[]
birler = [0]*d
sifirlar = [0]*d

for n in range(1,N):
    ad= 0 #seçilen ilan
    max_th= 0
    for i in range(0,d):
        rasbeta =random.betavariate ( birler[i]+1 ,sifirlar[i]+1)
        if rasbeta > max_th:
            max_th = rasbeta
            ad = i
    secilenler.append(ad)
    odul = veriler.values[n,ad]
    if odul == 1:
        birler[ad] += 1
    else:
        sifirlar[ad] += 1
    toplam += odul
print("Toplam Odul: ")
print(toplam)

plt.hist(secilenler)
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    