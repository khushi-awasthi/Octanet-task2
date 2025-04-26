# #dictionary comprehension
# squares={x:x**2 for x in range(1,6)}
# print(squares)
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
words=["cat", "dog", "apple", "bat"]
word={}
for i in words:
    length=len(i)
    if length in word:
        word[length].append(i)
    else:
        word[length]=[i]
print(word)

# Q3. Remove a key from a dictionary
# ● Input: {'a': 1, 'b': 2, 'c': 3}, remove 'b'
# ● Output: {'a': 1, 'c': 3}
d1={'a': 1, 'b': 2, 'c': 3}
d1.pop('b')
print(d1)

# Q4. Invert a dictionary (swap keys and values)
# ● Input: {'a': 1, 'b': 2}
# ● Output: {1: 'a', 2: 'b'}

# ● Assume values are unique
# Q5. Sort a dictionary by its values
# ● Input: {'a': 3, 'b': 1, 'c': 2}
# ● Output: {'b': 1, 'c': 2, 'a': 3}
# Q6. Count character frequency in a string
# ● Input: "banana"
# ● Output: {'b': 1, 'a': 3, 'n': 2}
# Q7. Count the number of unique characters in a string using a set
# ● Input: "hello"

# ● Output: {'h', 'e', 'l', 'o'}, Count: 4
# Q8. Get the common vowels in a sentence
# ● Input: "Hello Universe"
# ● Output: {'e', 'o', 'u'}
# Q9. Take a list of strings and return the set of words that appear
# in all strings
# ● Input: ["apple banana", "banana orange", "banana grape"]
# ● Output: {'banana'}
# Q10. Find the missing number(s) from a given range using a set
# ● Input: numbers = [1, 2, 4, 6], full_range = range(1,