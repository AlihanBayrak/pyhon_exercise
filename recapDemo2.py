# -*- coding: utf-8 -*-

sayi = int(input("Sayıyı giriniz : "))
asalMi = True

for x in range(2,sayi):
    if(sayi % x) == 0:
        asalMi = False
        break

if asalMi == True:
    print("ASAL")
else:
    print("ASAL DEĞİL")
