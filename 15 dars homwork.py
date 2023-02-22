# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:11:13 2023

@author: WINDOWS-11
"""
# talaba_0 = {
#     'name' : 'ali',
#     'lastname':'olimov',
#     'age': 30,
#     'facultet':'matematika',
#     'kursi':4
#     }

# for key, value in talaba_0.items():
#     print(f"Kalit soz - {key}")
#     print(f"Qiymati - {value}")


# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s12',
#     'olim' : 'mi 10 pro',
#     'hasan' : 'nokia 3310'
#     }

# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni - {value}")

# mahsulotlar = {
#     'olma' : 10000,
#     'uzum' : 25000,
#     'anor' : 12000,
#     'limon' : 8000,
#     'banan' : 24000
#     }

# print("Dokondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(f"{mahsulot.title()}")


# mahsulotlar = {
#     'olma' : 10000,
#     'uzum' : 25000,
#     'anor' : 12000,
#     'limon' : 8000,
#     'banan' : 24000
#     }

# bozorlik = ['anor', 'uzum', 'non', 'baliq']

# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} som")
        
# for buyurtma in bozorlik:
#     if buyurtma not in mahsulotlar:
#         print(f"iltimos, dokonizga {buyurtma} ham olib keling")

# Amaliyot
#1

# izohli_lugat = {
#     'float' : 'onlik son',
#     'if' : 'shartlarni tekshirish operatori',
#     'boolean' : 'mantiqiy qiymat',
#     'integer': 'butun son',
#     'for' : 'amal bajarish sikli'
#     }

# for key, value  in sorted(izohli_lugat.items()):
#     print(f" {key.title()} - {value.title()} ")

#2

countries = {
    'rossiya' : 'moskva',
    'aqsh' : 'washington',
    'italiya' : 'rim',
    'singapur' : 'singapur',
    'uzbekiston' : 'toshkent'
    }

key = input("istalgan davlatni kiriting: ").lower()
country = countries.get(key)
if country == None:
    print(f"Bazada {key.title()} davlati yoq!")
else:
    print(f"{key.title()}ning piytaxti {countries[key].title()} ")    

















