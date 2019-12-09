# -*- coding: utf-8 -*-
mesaj = "Selamunaleykum Dünya" #* 20 krakteden oluşur
print(mesaj[2:5]) #ikiden beşe kadar
yeniMesaj = mesaj[:2] #Baştan ikiye kadar
print(yeniMesaj)
# aslında bu yaptığımız işlemi substring() işlemidir.

print(len(mesaj)) #bize değişkenin karakter sayısını verir.

print(mesaj[19:20])
yeniMesaj_2 = mesaj[len(mesaj)-1:len(mesaj)]#yukardaki pritle aynı çıktıyı verir
print(yeniMesaj_2)



