# -*- coding: utf-8 -*-

setA = {1,2,3,4,5,6}
setB = {1,3,5,6,8,9}

print(setA | setB) #birleşim
print(setA.union(setB)) #birleşim

print(setA & setB) #kesişim
print(setA.intersection(setB)) #birleşim

print(setA - setB) #fark
print(setA.difference(setB)) #fark

print(setA ^ setB) #simetrik ayrım
print(setA.symmetric_difference(setB)) #simetrik ayrım
