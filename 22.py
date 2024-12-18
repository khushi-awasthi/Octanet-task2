# display multiplication table from 1-10------------------------>
# for i in range(1,11):
#         for j in range(1,11):
#                 k=i*j
#                 print(k,end=' ')
#         print()


#Function===================
# WAP  to addd 2 number using function.
# def add(num1,num2): #function signature
#     num3=num1+num2
#     print(num3)

# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# # add(34,2)
# add(n1,n2)

#WAP program  to print factorial of number using function.
def fact(num):
    factorial=1
    for i in range (1,num+1):
        factorial=factorial*i
        #i=i+1
        print(factorial)

n1=int(input("Enter a number"))
fact(n1)
#springboard=====================
def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    while number>0:
        rem=number%10
        sum_of_digits=sum_of_digits+rem
        number=number//10
    
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
# Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

# It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
# If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if num1==7:
        product=num2*num3
    elif num2==7:
        product=num3
    elif num3==7:
        product=-1
    else:
        product=num1*num2*num3
    
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)

# Write a python function to check whether three given numbers can form the sides of a triangle. 
# Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.
# #lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    if(num1+num2 <= num3) or (num1+num3 <= num2) or (num2+num3 <= num1):
        failure="Triangle can't be formed"
        return failure
    else:
        success:"Triangle can be formed"
        return success
    

    #Use the following messages to return the result wherever necessary
   # return success
   # return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
message=form_triangle(num1, num2, num3)
print(message)
