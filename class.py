# -*- coding: utf-8 -*-
#Ortak özellikleri ve fonksiyonları bir arada tutmamızı sağlar
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    def carpma(self,sayi1,sayi2):
        return sayi1 * sayi2
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2

matematik = Matematik()
print("Toplam = " +  str(matematik.topla(2,78)))    
