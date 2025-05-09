# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:17:35 2025

@author: user
"""

buxoriy = {'ism':'Abdulloh Muhammad Ismoil Buxoriy',
           
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome as sahih", "Al-Adab ul-mufrad", "At tarixiy kabir"]
            }

shayxmuhammadsodiqmuhammadyusuf = {'ism':'Muhammad Sodiq Muhammad Yusuf',
                                   'tyil':1952,
                                   'vyil':2015,
                                   'tjoy':'Andijon',
                                   'asarlar':['Tafsiri Hilol','Iymon','Aqoid','Hidoya']
                                   }

navoiy = {'ism':'Mir Alisher Navoiy',
          'tyil':'1441',
          'vyil':'1501',
          'tjoy':'Xirot',
          'asarlar':['Xamsa','Liso un Tayir','Mahbub ul Qulub','Munojot']
          }

shaxslar = [buxoriy, shayxmuhammadsodiqmuhammadyusuf, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)