# from collections import defaultdict
# def notpresent():
#     return "this key is not present"
# dt=defaultdict(notpresent)
# dt["A"]=123
# dt["B"]=234
# print(dt["B"])
# print(dt["Z"])

# Ordered dictionary
# from collections import OrderedDict
# print("this is a dict:\n")
# d={}
# d['a']=1
# d['b']=2

# for key,value in d.items():
#     print(key,value)
# print("\n ordered dict:\n")
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4
# for key,value in od.items():
#     print(key,value)
# Strings================
# name="Khushi Awasthi"
# print(name[-5])
# for ch in name:
#     print(ch)
# for i in range(len(name)):
#     
#     print(i)
# Write a program to print even position elements in strings
# clg=input("College name")
# for i in range(len(clg)):
#     if i%2==0:
#         print(i," ",clg[i])

#wap to print vowels---
# clg=input("College name")
# list1=['a','A','e','E','o','O','i','I','u','U']
# for i in range(len(clg)):
#     if clg [i] in list1:
#         print(i," ",clg[i])
# str=input("enter string")
# f1={}
# for ch in str:
#     if ch in f1:
#         f1[ch]=f1[ch]+1
#     else:
#         f1[ch]=1
# print(f1
#       )
# string slicing----------
# str="Python"
# print(str[1:5])
# str="Welcome to the world of python"
# print(str[2:10:1])
str1=input("Enter the string")
revstring=str1[::-1]
if str1==revstring:
    print("palindrome")
else:
    print("not palindrome")

