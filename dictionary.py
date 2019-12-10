# -*- coding: utf-8 -*-
#set gibi sırasız veri tutar

sozluk = {
        #"key" : "value",
        "red" : "kırmızı",
        "eraser" : "silgi"
        }

sozluk2 = dict(kitap ="book", masa ="table")

sozluk["red"] = "kırmızı1"
sozluk["pencil"] = "kalem"
del(sozluk)["red"]
print(sozluk)
print(sozluk2)

