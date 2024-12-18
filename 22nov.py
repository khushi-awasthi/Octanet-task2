# set
# set1={4,6,7,"hii"}
# print(set1)
# set1.remove(6)
# print(set1)
# set1.discard(9)
# print(set1)
# set1.pop()
# print(set1)
# a={1,2,3,4,5,6}
# b={9,8,7,6,5,1}
# print(a|b)
# print(a.union(b))
# print(a&b)
# print(a.intersection(b))
# print(a-b)
# print(a.difference(b))
# print(a^b)
# print(a.symmetric_difference(b))
# frozen set
a={1,2,3,4,5,'d'}
b=frozenset(a)
print(b)
print(type(a))
print(type(b))
# print(b.add(9))
a.add(9)
print(a)