# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:55:17 2023

@author: WINDOWS-11
"""


# while - toki

# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son+=1
# print('dastur tugadi')

#2-misol sonni kvadratini hisoblash

savol = "Istalgan sonni kiriting "
savol+= "dasturdan chiqish - 'exit' "

qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)