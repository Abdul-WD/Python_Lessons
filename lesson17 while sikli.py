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

# savol = "Istalgan sonni kiriting "
# savol+= "dasturdan chiqish - 'exit' "

# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

#Amaliyot

# savol = "Dasturni toxtatish uchun 'stop' sozini yozing\n" 
# savol+= 'Siz yoqtirgan asar:'

# natija = ''
# while natija != 'stop':
#     natija = input(savol)
# print('Dastur toxtatildi')

savol = "'exit' - dasturdan chiqish\n"
savol+= "Yoshingiz nechida? >>> "

while True:
    qiymat = input(savol)
    if qiymat == "exit" or qiymat == "quit":
        break
    
    yosh = int(qiymat)
    
    if yosh < 7:
        narh = 2000
    elif 7 <= yosh < 18:
        narh = 3000
    elif 18<= yosh < 66:
        narh = 10000
    else:
        narh = 0
        
    if narh == 0:
        print("Sizga bilet bepul")
        
    else:
        print(f"Bilet {narh} som")






















