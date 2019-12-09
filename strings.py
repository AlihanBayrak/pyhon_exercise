# -*- coding: utf-8 -*-
mesaj = "Selamunaleykum Dünya" #* 20 krakteden oluşur
print(mesaj[2:5]) #ikiden beşe kadar
yeniMesaj = mesaj[:2] #Baştan ikiye kadar
print(yeniMesaj)
# aslında bu yaptığımız işlemi substring() işlemidir.


#len
print(len(mesaj)) #bize değişkenin karakter sayısını verir.
print(mesaj[19:20])
yeniMesaj_2 = mesaj[len(mesaj)-1:len(mesaj)]#yukardaki pritle aynı çıktıyı verir
print(yeniMesaj_2)

#lower upper
print(mesaj.upper())
print(mesaj.lower())

#replace()
print(mesaj.replace("u", "ü"))

#Split() ve Strip()
information = "     Alihan;Bayrak;19;Erzurum ".strip()
print(information.split())# split() ile kelime kelime stringlerine ayırıyoruz
print("Adı = " + information.split(";")[0])


