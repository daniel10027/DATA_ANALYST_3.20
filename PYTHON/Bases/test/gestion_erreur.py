#coding:utf-8

age = input("votre age")
try:
    age=int(age)
except:
    print("age incorrect")
else:
    print("age=",age)