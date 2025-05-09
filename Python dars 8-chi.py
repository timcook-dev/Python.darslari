# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 20:24:43 2025

@author: user
"""

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan,' 'Olim']

for mehmon in mehmonlar:
    print("Salom", mehmon)
    print("Hayr", mehmon)
    
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
    
print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
        
    


