# -*- coding: utf-8 -*-


#%%
def dikUcgenHesapla(a,b):
    return a*b/2

alan = dikUcgenHesapla(5,6)

print(alan)
#%%

dikUcgenHesapla2 = lambda a,b : a*b/2

print(dikUcgenHesapla2(3,6))
print(type(dikUcgenHesapla2))

x = dikUcgenHesapla2
print(x(4,5))