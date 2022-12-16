# project 1 = Ecom

import pickle

book= []
fr = open("data1.txt","r")
list1 = fr.readlines()
for each in list1:
    a= each.split()
    print(a)
fr.close()

