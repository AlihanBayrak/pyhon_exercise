# -*- coding: utf-8 -*-
#listelere benzerdir
#tek farkı listelerde elemanları değiştirebiliyorken
#tuple de değiştime olmaz
#bu veri yapısı performanlı bir data sağlar

tupleListe = (3,6,9,"Erzurum",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0] = 6
#tupleListe[0] = 6 //hata

print(tupleListe[-2])
print(liste[-2])

print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)