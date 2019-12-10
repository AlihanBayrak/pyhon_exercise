# -*- coding: utf-8 -*-

sayi = int(input("Sayı : "))

faktoriyel = 1

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanmaz")
elif sayi == 0:
    print("Sonuc : 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuc : ",faktoriyel)