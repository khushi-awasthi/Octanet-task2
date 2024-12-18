# gfg="geeksforgeeks"
# gfg="".join(reversed(gfg))
# print(gfg)
# s1="heelloee"
# print(s1.isalnum())
# print(s1.isalpha())
# print(s1.isdigit())
# print(s1.islower())
# print(s1.isupper())
# print(s1.lower())
# print(s1.upper())
# print(s1.replace("ee","e"))
# print(s1.replace("ee","e",1))
# print(s1.split())
# print(s1.swapcase())
# str1="hello i am the best"
# strlist=str1.split()
# print(strlist)
# str1="hello @i @am the best"
# strlist=str1.split("@")
# print(strlist)

# count vowel in each word-----------
# s1=input("Enter the string")
# strlist=s1.split()
# vowel=["a","e","i","o","u","A","E","I","O","U"]
# count=0
# for ele in strlist:
#     for i in ele:
#         if i in vowel:
#             count=count+1
#     print(ele,"has",count,"vowels")
#     count=0

# upper case and lower case-------------
# s1=input("Enter the string")

# count1=0
# count2=0
# for i in s1:
#     if(i.islower()):
#         count1=count1+1
#     elif(i.isupper()):
#         count2=count2+1
# print("The number of lowercase character is:")
# print(count1)
# print("The number of uppercase character is:")
# print(count2)

# palindrome

# String immutable-------------
# str="hello "
# str[6]="j"
# error:object does not support item assignment
# s1=str.replace("h","H")
# print(s1)
# =====================
# s1="I am a student"
# print(s1.capitalize())
# print(s1.title())
# print(s1.count())
# s1="Hel@lo khg@ jbjh @jhjh@ jbjg"
# # print(s1.count('l'))
# # endstr=s1.endswith('o')
# # strstr=s1.startswith('H')
# # print(strstr)
# # print(endstr)
# print(s1.split("@",2))
# print(s1.rsplit("@",4))
# s2="i \n am\n a \n student\n of \n psit"
# print(s2.splitlines())
# list=["a","b","c"]
# result=",".join(list)
# print(result)
# str="Hellopython"
# s1=str[0:2]
# print(s1)
# s2=str[-1:-3]
# print(s1+s2)
# str2="gh"
# print(str2+str2)
# str3="w"
# l=len(str3)
# if l<2:
#     print("empty string")
s1=input("Enter the string")
if len(s1)<3:
    print(s1)
elif(s1.endswith('ing')):
    print(s1+"ly")
else:
    print(s1+"ing")
