# -*- coding: utf-8 -*-
#listelere benzerdir 
#indexsiz ve sırasız elemanlardan oluşmasıdır
#veri tekrararı olamaz, performanslıdır

ogrenciSet = {"Alihan", "Arzu", "Aydın", "Yasin"}
print(ogrenciSet)

for ogrenci in ogrenciSet:
    print(ogrenci)
print("Alihan" in ogrenciSet)

if "Alihan" in ogrenciSet:
    print("Listede var")
    
ogrenciSet.add("Recep")
print(ogrenciSet)

ogrenciSet.update(["Emsile","Şeyma","Gül"])
print(ogrenciSet)

print(len(ogrenciSet))

ogrenciSet.remove("Recep")
print(len(ogrenciSet))

ogrenciSet.discard("Recep") #sıkıntı yapma
print(len(ogrenciSet))

x = ogrenciSet.pop() #son elemanı siler
print(len(ogrenciSet))
print(ogrenciSet)
