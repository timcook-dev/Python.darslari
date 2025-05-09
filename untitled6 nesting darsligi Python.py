# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:25:08 2025

@author: user
"""

davlatlar = {
    'ozbekiston':{'poytaxti':'toshkent',
                  'maydon':448798,
                  'aholi':33_000_000,
                  'pul birligi':'som'},
    'rossiya':{'poytaxti':'moskva',
               'maydon':17_098_246,
               'aholi':144_000_000,
               'pul birligi':'rubl'},
    'malaysiya':{'poytaxti':'kuala lumpur',
                 'maydon':329750,
                 'aholi':25_000_000,
                 'pul birligi':'ringgit'}}


davlat = input('Davlat nomini kriting:').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxt {info['poytaxti'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print('Bizda bu davlat haqida malumot mavjud emas')