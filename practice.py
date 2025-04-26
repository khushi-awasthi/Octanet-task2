#sum of two numbers-------------->
# num1=10
# num2=22
# print(num1+num2)

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# sum=int(num1)+int(num2)
# print("sum of {0} and {1} is {2}" .format(num1,num2,sum))

#Maximum of two numbers---------->

# num1=5
# num2=9
# if(num1>num2):
#     print("num1 is maximum")
# else:
#     print("num2 is maximum")

# num1=input("enter first number")
# num2=input("enter second number")
# # if(num1>num2):
# #     print("num1 is maximum")
# # else:
# #     print("num2 is maximum")

# # maximum=max(num1,num2)
# # print(maximum)
# print(num1 if num1>=num2 else num2)

#Factorial of number---------->

# num=int(input("enter any number"))
# factorial=1
# for i in range (1,num+1):
#     factorial=factorial*i
#     # i=i+1
# print(f"The factorial of{num} is {factorial}")

#Simple interest---------->
# p=int(input("enter the principal amt."))
# r=int(input("enter the rate of interest"))
# t=int(input("enter time"))
# SI=(p*r*t)/100
# print(SI)

#Armstrong number--------->

# number = int(input("enter any number"))

# # Convert the number to a string to easily access each digit
# num_str = str(number)

# # Get the number of digits
# num_digits = len(num_str)

# # Initialize sum to 0
# total_sum = 0

# # Loop through each digit, raise it to the power of num_digits, and add it to the total_sum
# for digit in num_str:
#     total_sum += int(digit) ** num_digits

# # Check if the total_sum is equal to the original number
# if total_sum == number:
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")



