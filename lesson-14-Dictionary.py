# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:12:03 2023

@author: WINDOWS-11
"""


# car_0 = {'model' : 'Ferrari', 'color' : 'red'}
# print(car_0['model'])

# talaba_0 = {'name' : 'Abror', 'age' : 25, 'course' : '4-kurs'}
# talaba_0['fakultet'] = 'informatika' 
# print(f" {talaba_0['name'].title()},\
# {talaba_0['age']} yoshda. U {talaba_0['course']}da, \
# {talaba_0['fakultet'].title()} fakultetida o`qiydi.")

#Amaliyot
# #1
# friend = {'name': 'Anvar', 'age':'36', 'kasbi': 'dasturchi'}
# print(f"{friend['name'].title()} mening dostim. \
# U {friend['age']} yoshda. {friend['kasbi'].title()} bo`lib ishlaydi.")

#2
python_dictionary = {
    'integer': 'butun son', 
    'float': 'onlik son',
    'if':'"agar" shart operatori',
    'str':'matn-ozgaruvchi turi'
    }

# key = input('Kalit soz kiriting: ').lower()
# print(python_dictionary.get(key, "Bunday kalit soz mavjud emas!"))

key = input('Kalit soz kiriting: ').lower()
tarjima = python_dictionary.get(key)
if tarjima == None:
    print("Bunday soz mavjud emas!")
else:
    print(f" {key.title()} sozi {tarjima} deb tarjima qilinadi.")




# if key in python_dictionary:
#     result = python_dictionary[key]
#     print(result)
# else:
#     print('Bunday kalit soz mavjud emas!')


























