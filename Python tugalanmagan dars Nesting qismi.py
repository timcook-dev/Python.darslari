# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 19:33:03 2025

@author: user
"""
buxoriy = {'ism':'Abu Muhammad ibn Ismoil',
           'tyil': 810,
           'vyil': 870,
           'tjoy': 'Buxoro'
           }

qodiriy = {'ism':'Abdulloh Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent'
           }

muhammadsodiqmuhammadyusuf = {'ism':'Shayx Muhammad Sodiq Muhammad Yusuf,',
                                 'tyil':1952,
                                 'vyil':2015,
                                 'tjoy':'Andijon'
                                 }
navoiy = {'ism':'Alisher Navoiy',
          'tyil':1441,
          'vyil':1501,
          'tjoy':'Xirot'
          }


shaxslar = [buxoriy, qodiriy,muhammadsodiqmuhammadyusuf, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    tjoy = shaxs['tjoy']
    print(f"{ism} {tyil}-yilda tavalud topgan\n tugilgan viloyati {tjoy}\n {vyil-tyil} yil umr korgan.Alloh rahmatiga olgur,\n barchalaridan Alloh rozi bolsin qilgan jamiyki ezgu niyatlarini dargohida qabul aylasin.Amin.")
              
kitoblar = {
    'buxoriy':['Sahihul Buxoriy'],
    'qodiriy':['Mehrobdan Chayon'],
    'muhammadsodiqmuhammadyusuf':['Oltin Silsila'],
    'navoiy':['Hamsa']}


          