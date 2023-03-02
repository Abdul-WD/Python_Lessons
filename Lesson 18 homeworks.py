# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:38:19 2023

@author: WINDOWS-11
"""

#Amaliyot1
# print("Maxsulotlar ro`yxatini tuzamiz!")
# maxsulotlar = []
# n = 1
# while True:
#     savol = "Maxsulot nomini kiriting: "
#     maxsulot = input(savol)
#     maxsulotlar.append(maxsulot)
#     takror = input("Yana maxsulot qo`shasizmi? (ha / yo`q) ")
#     if takror == 'ha':
#         continue
#     else:
#         break
# print("Buyurtma bergan maxsulotlaringiz:")
# for key in maxsulotlar:
#     print(f"{n}. {key.title()}")
#     n+=1

#Amaliyot2

# print("e-bozor maxsulotlari va narxlari")
# e_bozor = {}
# while True:
#     maxsulot = input("Maxsulot nomi: ")
#     narx = input(f"{maxsulot.title()}ning narxi: ")
#     e_bozor[maxsulot] = int(narx)
#     takror = input("Davom etasizmi? (ha / yo`q) ")
#     if takror != 'ha':
#         break
# print("dastur to`xtatildi!")
# print("E-bozor maxsulotlari:")
# for key, value in e_bozor.items():
#     print(f"{key.title()} - narxi {value} so`m.")

#Amaliyot 3

buyurtmalar = ['olma', 'non', 'gosht', 'tuxum']
e_bozor = {}
while True:
    maxsulot = input("Maxsulot nomi: ")
    narx = input(f"{maxsulot.title()} narxi: ")
    e_bozor[maxsulot] = int(narx)
    takror = input("davom etamiz: (ha/yuq) ")
    if takror != 'ha':
        break

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in e_bozor.keys():
        narx = e_bozor[buyurtma] 
        print(f"{buyurtma.title()} narxi {narx} so`m")
    else:
        print(f"{buyurtma} mahsuloti bizda yuq!")



















