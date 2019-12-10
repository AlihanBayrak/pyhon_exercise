# -*- coding: utf-8 -*-

sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz :"))
sayi3 = int(input("Üçüncü sayıyı giriniz :"))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = sayi1
elif (sayi2 >= sayi3) and (sayi2 >= sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
    
print("En Büyük :",enBuyuk)