# -*- coding: utf-8 -*-

import random
def haromszog():
    szamok =[]
    for i in range(3):
        szamok.append(random.randint(2,15))
    
    feladat = 'Megszerkeszthető-e a háromszög '+ str(szamok[0]) +', '+ str(szamok[1]) +', '+ str(szamok[2]) +' oldalakból?'
    
    megoldas = szamok[0] + szamok[1] > szamok[2] and szamok[1] + szamok[2] > szamok[0] and szamok[0]+szamok[2] > szamok[1]
    
    
    
    return feladat, megoldas

feladat, megoldas = haromszog()
print(feladat)
print('Igen / Nem')
print('A helyes megoldás: '+str(megoldas))