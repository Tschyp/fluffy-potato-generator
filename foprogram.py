# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:26:59 2016

@author: user
"""
pontok = 0
import haromszog


feladat, megoldas = haromszog.haromszog()
print(feladat)

valasz=bool(raw_input('Megoldas:'))

if valasz == megoldas:
	print("Helyes!")
	pontok = pontok + 1
print(pontok)


import ...	