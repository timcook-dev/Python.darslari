# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:17 2025

@author: user
"""

davlatlar = {
    'ozbekiston':{'poytaxt':'toshkent',
                  'maydon':448978,
                  'aholi':33_000_000,
                  'pul birligi':'som'},
    'rosiya':{'poytaxt':'moskva',
                      'maydon':17_098_246,
                      'aholi':144_000_000,
                      'pul birligi':'rubl'},
    'aqsh':{'poytaxt':'vaashington',
                      'maydon':9_631_418,
                      'aholi':327_000_000,
                      'pul birligi':'dollar'},
    'malaysiya':{'poytaxt':'kuala lumpur',
                 'maydon':329750,
                 'aholi':25_000_000,
                 'pul birligi':'ringgit'}
}
 
for davlat, info in davlatlar.items():
    if davlat.lower() == 'aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
     
        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")

        
          