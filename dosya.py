# -*- coding: utf-8 -*-

f = open("hakunaMatata.txt")

#print(f.read(10))
print("------------")
print(f.readline()) #satır okuma

f.close()


#r Read, a append, w write, x create,

fileToAppend = open("hakunaMatata.txt","a")
fileToAppend.write("\n")
fileToAppend.write("Yasin")
fileToAppend.close()


