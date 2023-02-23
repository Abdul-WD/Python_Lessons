# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:04:11 2023

@author: WINDOWS-11
"""


# malibus = []

# for n in range(10):
#     new_car = {
#         'model': 'malibu',
#         'rangi': None,
#         'yil' : 2022,
#         'narxi' : None,
#         'km' : 0,
#         'karobka' : 'avto'
#         }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rangi'] = 'oq'
    
# for malibu in malibus[3:6]:
#     malibu['rangi'] = 'qora'
    
# for malibu in malibus[6:]:
#     malibu['rangi'] = 'qora'
#     malibu['karobka'] = 'mexanika'
    
# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narxi'] = 45000
#     else:
#         malibu['narxi'] = 40000
    
# for malibu in malibus:
#     print(malibu)

# developers = {
#     'ali' : ['python', 'c++'],
#     'vali' : ['html', 'css', 'js'],
#     'hasan' : ['php', 'sql'],
#     'maryam' : ['c++', 'c#'],
#     'husan' : ['python', 'php']
#     }

# for developer, language in developers.items():
#     print(f"\n{developer.title()} quyidagi dasturlash tillarini biladi: ", end='')
#     for til in language:
#         print(f"{til.upper() }", end=' ')


#Amaliyot
shaxs_1 = {
    'name' : "Abu Abdulloh Muhammad ibn Ismoil",
    't_yili' : 810,
    't_joyi' : 'Buxoro',
    'yoshi' : 60
    }

shaxs_2 = {
    'name' : "Abdulla Qodiriy",
    't_yili' : 1984,
    't_joyi' : 'Toshkent',
    'yoshi' : 44
    }

shaxs_3 = {
    'name' : "Erkin Vohidov",
    't_yili' : 1936,
    't_joyi' : 'Fargona',
    'yoshi' : 80
    }

shaxs_4 = {
    'name' : "Alisher Navoiy",
    't_yili' : 1441,
    't_joyi' : 'Xirot',
    'yoshi' : 60
    }

mashxurlar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4]
for shaxs in mashxurlar:
    ism = shaxs['name']
    tyil = shaxs['t_yili']
    tjoyi = shaxs['t_joyi']
    umri = shaxs['yoshi']
    print(f"{ism} {tyil}-yilda {tjoyi}da tavallud topgan. {umri} yil umr korgan.")
    






















