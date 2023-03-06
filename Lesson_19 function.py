# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:50:22 2023

@author: WINDOWS-11
"""


#funksiyalar

# def salom_ber(ism):
#     '''salom berish funksiyasi'''
#     print(f"Assalomu alaykum, {ism.title()}")

# salom_ber('anvar')

#Amaliyotlar
#1

# def t_y_hisobla(ism, yoshi):
#     '''Tugilgan yilini hisoblash funksiyasi'''
#     print(f"{ism.title()} {2023-yoshi} yili tugilgan")
    
# t_y_hisobla('alijon', 25)

# #2
# def hisobla(son):
#     '''sonning kvadrati va kubini hisoblash funksiyasi'''
#     print(f"{son} ning kvadrati: {son**2}\n"
#           f"{son} ning kubi: {son**3}")

# hisobla(3)

#3

# def j_t_hisobla(son):
#     '''Sonning juft yoki toqligini hisoblash funksiyasi'''
#     if son % 2 == 0:
#         print(f"{son} soni juft son")
#     else:
#         print(f"{son} soni toq son")
# j_t_hisobla(2)

#4

# def kattasi(son1, son2):
#     '''2 ta sondan kattasini aniqlash'''
#     if son1 > son2:
#         print(f"{son1} kattasi")
#     elif son1 < son2:
#         print(f"{son2} kattasi")
#     else:
#         print(f"sonlar teng")

# kattasi(34, 24)
# kattasi(54, 54)
# kattasi(1, 100)

#5

def hisobla(son1, son2 = 2):
    print(f"{son1} ning {son2}-darajasi = {son1**son2}")
    
hisobla(8, 3)




























