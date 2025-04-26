#Q1. Find the second largest number in a list.
numbers = [5, 3, 8, 6]

first = second = -1
for i in range(len(numbers)):
    num = numbers[i]
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest number:", second)
# ----------------------------------------------------------------------------------------------------------------

#Q2. Reverse a list without using reverse() or slicing.

my_list = [8,9,7]
start = 0
end = len(my_list) - 1

while start < end:
    temp = my_list[start]
    my_list[start] = my_list[end]
    my_list[end] = temp

    start += 1
    end -= 1
print("Reversed list:", my_list)
# --------------------------------------------------------------------------------------------------------------

#Q3. Count how many times a value appears in a tuple.
t = (1, 1, 2, 3,1)
value = 1
count = 0
for i in range(len(t)):
    if t[i] == value:
        count += 1
print("The value", value, "appears", count, "times.")
# ---------------------------------------------------------------------------------------------------------------

#Q4. Find the index of the first occurrence of an element.
my_list = [10, 20, 30, 20]
value = 20
index = -1
for i in range(len(my_list)):
    if my_list[i] == value:
        index = i
        break
print("The first occurrence of", value, "is at index:", index)
------------------------------------------------------------------------------------------------------------------

#Q5. Replace all even numbers in a list with 0.
my_list = [1, 2, 3, 4,6]
for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = 0
print("List after replacing even numbers with 0:", my_list)
# -----------------------------------------------------------------------------------------------------------------

#Q6. Remove all occurrences of a specific element from a list.
my_list = [1, 2, 2, 3]
element_to_remove = 2
new_list = []
for i in range(len(my_list)):
    if my_list[i] != element_to_remove:
        new_list.append(my_list[i])
print("List after removing", element_to_remove, ":", new_list)
# -------------------------------------------------------------------------------------------------------------

#Q7. Remove the smallest value entry from a dictionary.

my_dict = {'a': 10, 'b': 5, 'c': 8}
smallest_value = -1
smallest_key = None
for key in my_dict:
    if my_dict[key] < smallest_value:
        smallest_value = my_dict[key]
        smallest_key = key
new_dict = {}
for key in my_dict:
    if key != smallest_key:
        new_dict[key] = my_dict[key]
print("Dictionary after removing smallest value entry:", new_dict)

# ----------------------------------------------------------------------------------------------------------------

#Q8. Reverse each string in a list of strings.
string_list = ["abc", "xyz"]
reversed_list = []
for s in string_list:
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    reversed_list.append(reversed_str)

print("Reversed strings:", reversed_list)

# -------------------------------------------------------------------------------------------------------------

#Q9. Convert a list of tuples into a dictionary with summed values if keys repeat.

tuple_list = [('a', 2), ('b', 3), ('a', 4)]
result_dict = {}
for key, value in tuple_list:
    if key in result_dict:
        result_dict[key] += value
    else:
        result_dict[key] = value
print("Resulting dictionary:", result_dict)

# --------------------------------------------------------------------------------------------------------------------

#Q10. Sort a tuple of numbers in descending order.

t = (3, 1, 4)

sorted_tuple = tuple(sorted(t, reverse=True))
print("Sorted tuple in descending order:", sorted_tuple)







