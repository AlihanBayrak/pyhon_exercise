# -*- coding: utf-8 -*-
#Ortak özellikleri ve fonksiyonları bir arada tutmamızı sağlar

#%%
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
#%% property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Alihan","Bayrak","19")
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
Aydın= Worker()
Yasin = Customer()