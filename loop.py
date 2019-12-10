# -*- coding: utf-8 -*-
#Benzer işlemleri belirli bir şarta göre tekrarlamak için kullnılır

#list of numbers
numbers = [1,2,5,6,8,9,12,15,16]

# variable to store the sum
sum = 0

#iterate over the list
for val in numbers:
    sum = sum+val

#output: The sum is 74    
print("The sum is", sum)