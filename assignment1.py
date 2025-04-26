# 1. Write a program to find the maximum and minimum elements in a list.
# list1=[9,5,7,84,3,22,66]
# x=min(list1)
# print(x)
# y=max(list1)
# print(y)
# 2. Create a new list with only the even numbers from an existing list.
# list1=[1,2,3,4,5,6,7]
# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print("even number list:",list2)
# ---------------
# list1=[1,2,3,4,5,6,7]
# newlist=[i for i in list1 if i%2==0 ]
# print(newlist)

# 3. Remove all duplicate elements from a list.
# l1=[1,2,2,3,3,4,5,5,6,5,6]
# x=list(set(l1))
# print(x)
# l1=[1,2,2,3,3,4,5,5,6,5,6]
# z=[]
# for i in l1:
#     if i not in z:
#         z.append(i)
# print("list after removing the duplicate elements",z)

# 4. Find the index of a specific element in a list.
# l=['a','b','c','d']
# print(l.index('c'))

# l=['a','b','c','d']
# e ='z'
# if e in l:
#     index=l.index(e)
#     print(f"index of{e} is :",index)
# else:
#     print(f"index of {e} is not found in list")

# 5. Merge two lists into one.
# l1=[1,2,3,4]
# l2=[9,8,7,6,5]
# for i in l2:
#     l1.append(i)
# print(l1)

# l1=[1,2,3,4]
# l2=[9,8,7,6,5]
# l1.extend(l2)
# print(l1)


# 6. Write a program to sum all the elements in a list.
# l1=[1,2,3,4,5]
# sum=0
# for i in l1:
#     sum=sum+i
# print(sum)

# 7. Rotate a list to the right by k positions.
# l1 = [1, 2, 3, 4, 5,6,7]
# k = 3
# rotate_right = l1[-k:] + l1[:-k]
# print(rotate_right)

# 8. Create a list of squares for numbers from 1 to 10 using list comprehension.
# square = [a**2 for a in range(1, 11)]
# print(square)

# 9. Find the common elements between two lists.
# l1=[1,2,3,4,5]
# l2=[2,4,5,9,8]
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)

# print("Common elements using loop method:", l3)
l1=[1,2,3,4,5]
l2=[2,4,5,9,8]
l3=[i for i in l1 if i in l2]
print(l3)