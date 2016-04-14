# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:55:35 2016

@author: user
"""
import random
def logika1():
    szereplok = ['Jakab','Gizi','Béla','Panka','Csenger','Vera']
    aktualis = random.sample(szereplok, 3)    
    lehet = random.sample(aktualis, len(aktualis))    
    lehet = [ aktualis[i] for i in range(len(aktualis))]
    feladat = 'Van három testvér. '+", ".join(lehet)+'. A következőket tudjuk róluk:' + "\n"
    for i in range(len(aktualis)-1):
        if random.choice([1,2])==1:
            feladat += aktualis[i]+' magasabb mint '+aktualis[i+1]+"\n"
        else:
            feladat += aktualis[i+1]+" alacsonyabb mint "+aktualis[i]+"\n"
    #print(feladat)
    kerdesek = ['legmagasabb','középső','legalacsonyabb']
    kerdes = random.randint(0,len(kerdesek)-1)
    feladat +='Szerinted melyikük a '+kerdesek[kerdes]+'?'
    for i in aktualis:
        print(i)
    feladat += 'A helyes megoldás: '+aktualis[kerdes]
    return feladat, lehet, lehet.index(aktualis[jo])

feladat, lehet, jo = logika1()
print(feladat)
print(lehet)
print('A helyes megoldás: '+lehet[jo])