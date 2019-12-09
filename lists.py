# -*- coding: utf-8 -*-

#ogrenci1 = "Alihan"
#ogrenci2 = "Aydın"
#ogrenci3 = "Arzu"
#ogrenci4 = "Yasin"
#
#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)
#print(ogrenci4)

ogrenciler = ["Alihan", "Aydın", "Arzu", "Yasin"]

ogrenciler.append("Talha")
print(ogrenciler[3]) #Yasin
ogrenciler.remove("Yasin")
print(ogrenciler)

#list constructor(oluşturucu)
sehirler = list(("Erzurum", "İstanbul", "Erzurum"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
#print(sehirler.clear()) #temizlendi :)
print("Erzurum sayısı = " + str(sehirler.count("Erzurum")))
print("Erzurum indexi = " + str(sehirler.index("Erzurum")))
sehirler.pop(1) # çıktı
sehirler.insert(0, "İstanbul") #ekleme
sehirler.reverse() # takla attırma :) ['Erzurum', 'Erzurum', 'İstanbul']
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0] = "İzmir"
print(sehirler2)
print(sehirler)
print(sehirler3)


