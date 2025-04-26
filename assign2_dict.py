# ,list comprehension
# syntax-->
#   newlist =[expression for itmems in iterable if condition = true]
# boss=["dr","rty","rte","tr"]
# newlist=[]
# for i in boss:
#     if "t" in i:
#         newlist.append(i)
# print(newlist)

# boss=["dr","rty","rte","tr"]
# newlist=[i for i in boss if "t" in i]
# print(newlist)

#     dictionary    # 

dict={"brand":"maruti","electric":"false","year":2014,"color":"red"}
# print(dict)
# print(len(dict))
# print(type(dict))
# mine=dict(name="Khushi",age=21,color="black")
# print(mine)
# x=dict["brand"]
# print(x)
# y=dict.keys()
# print(y)
# z=dict.values()
# print(z)
# dict["bg-color"]="black"
# print(y)
# p=dict.items()
# print(p)
# dict["color"]="white"
# print(dict)
# dict["colors"]="white"
# print(dict)
# if "brand" in dict:
#     print("yes, it is present")
# dict.update({"brand":"KIA"})
# print(dict)
# dict.pop("brand")
# print(dict)
# dict.popitem()
# print(dict)
# del dict
# print(dict)

# ASSIGNMENT - 02

# Q1. Count frequency of each word in a sentence
# ● Input: "this is a test this is only a test"
# ● Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
# d1="this is a test this is only a test"
# a=d1.split()
# d2={}
# for item in a:
#     if item in d2:
#         d2[item]+=1
#     else:
#         d2[item]=1
# print(d2)

   
# Q2. Group words by their length using dictionary
# ● Input: ["cat", "dog", "apple", "bat"]
# ● Output: {3: ['cat', 'dog', 'bat'], 5: ['apple']}
# words=["cat", "dog", "apple", "bat"]
# word={}
# for i in words:
#     length=len(i)
#     if length in word:
#         word[length].append(i)
#     else:
#         word[length]=[i]
# print(word)
# Q3. Remove a key from a dictionary
# ● Input: {'a': 1, 'b': 2, 'c': 3}, remove 'b'
# ● Output: {'a': 1, 'c': 3}
# d1={'a': 1, 'b': 2, 'c': 3}
# r='b'
# if r in d1:
#     del d1[r]
# print(d1)

# Q4. Invert a dictionary (swap keys and values)
# ● Input: {'a': 1, 'b': 2}
# ● Output: {1: 'a', 2: 'b'}
# original_dict={'a': 1, 'b': 2}
# inverted_dict={value:key for key, value in original_dict.items()}
# print(inverted_dict)

# original_dict={'a': 1, 'b': 2}
# inverted_dict={}
# for key, value in original_dict.items():
#     inverted_dict[value]=key
# print(inverted_dict)

# ● Assume values are unique
# Q5. Sort a dictionary by its values
# ● Input: {'a': 3, 'b': 1, 'c': 2}
# ● Output: {'b': 1, 'c': 2, 'a': 3}
# Q6. Count character frequency in a string
# ● Input: "banana"
# ● Output: {'b': 1, 'a': 3, 'n': 2}
# s="banana"
# s1={}
# for i in s:
#     if i in s1:
#         s1[i]+=1
#     else:
#         s1[i]=1
# print(s1)
# Q7. Count the number of unique characters in a string using a set
# ● Input: "hello"
# ● Output: {'h', 'e', 'l', 'o'}, Count: 4
# d1="hello"
# d2=set(d1)
# print(d2)
# print("count=",len(d2))
# Q8. Get the common vowels in a sentence
# ● Input: "Hello Universe"
# ● Output: {'e', 'o', 'u','i'}
# d1="Hello Universe".lower()
# vowels={'a','e','i','o','u'}
# common_values={char for char in d1 if char in vowels}
# print(common_values)
# ===================
# d1="Hello Universe"
# d1.lower()
# d2={}
# vowel={'a','e','i','o','u'}
# for char in d1:
#     if char in vowel:
#         d2.append(char)
# print(d2)
        
# Q9. Take a list of strings and return the set of words that appear
# in all strings
# ● Input: ["apple banana", "banana orange", "banana grape"]
# ● Output: {'banana'}
# sentences=["apple banana", "banana orange", "banana grape"]
# common_words=set(sentences[0].split())
# for sentence in sentences [1:]:
#     words=set(sentence.split())
#     common_words=common_words.intersection(words)
# print(common_words)


# Q10. Find the missing number(s) from a given range using a set
# ● Input: numbers = [1, 2, 4, 6], full_range = range(1, 7)
# ● Output: {3, 5}
numbers = [1, 2, 4, 6]
for i in range(1,7):
    



# list = ['a','b','a','c','d','c','c']
# frequency = {}
# for item in list:
#    if (item in frequency):
#       frequency[item] += 1
#    else:
#       frequency[item] = 1
# print(frequency)