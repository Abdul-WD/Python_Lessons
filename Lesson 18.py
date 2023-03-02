# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:11:30 2023

@author: WINDOWS-11
"""

#1-usul

# print("Dostlar ruyxatini tuzamiz")
# friends =[]
# n = 1
# while True:
#     savol = f"{n}-dostingiz ismi: "
#     name = input(savol)
#     friends.append(name)
#     takrorlash = input("Yana ism qoshasizmi? ha / yoq ")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print('Sizning dostlaringiz royxati:')
# for friend in friends:
#     print(friend.title())


#2-usul
# print('dostlaringiz ruyxatini tuzamiz')
# dostlar = []
# n = 1
# while True:
#     savol = f"{n}-dostingiz ismi? "
#     ism = input(savol)
#     dostlar.append(ism)
#     takrorlash = input("yana ism kiritasizmi? (ha / yuq)\n")
#     if takrorlash == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("dostlaringiz:")
# for dost in dostlar:
#     print(dost.title())


#lugatni tuldirish

# print('dostlaringiz haqida malumot toplash')
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("do'stiz ismi?" )
#     yosh = input(f"{ism.title()}ning yoshi? ")
#     dostlar[ism] = int(yosh)
#     takror = input('Yana ism qushasizmi? (ha / yoq) ')
#     if takror == 'yoq':
#         ishora = False
# print("Dostlariz:")
# for key, value in dostlar.items():
#     print(f"{key.title()} {value} yoshda.")

talabalar = ['hasan' , 'husan', 'olim', 'anvar', 'kozim']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
print("Barcha talaba baholandi!")

print("talabalar bahosi:")
for key, value in baholangan_talabalar.items():
    print(f"{key.title()} bahosi {value}")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    