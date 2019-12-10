# -*- coding: utf-8 -*-
sayi = int(input("Kaç basamak yıldız olsun?"))

yildiz = ""

for x in range(1,sayi + 1):
    yildiz = yildiz + "*"
    print(yildiz)
