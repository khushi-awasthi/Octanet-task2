# print("line1")
# print("line1")
# print("line1")
# print("line1")
# try:
#     x=6/0
# except:
#     print("exception occur")
# print("line1")
# print("line1")
# print("line1")
# print("line1")
# print("line1")

# try:
    

    
#     print(9/3)
#     x="4"
#     h=int(x)
#     salary=300000
#     print(salary)
#     print("Exception is the powerful mechanism")
# except NameError:                         #generic accept block
#         print("name error is occured")
# except ValueError:                         
#         print("value error is occured")
# except ZeroDivisionError:                         
#         print("zero error is occured")
# else:
#     print("there is no exception")

#=======================================
# try:
#         name="abc"
#         print(name)
#         print(9/0)
# except NameError:
#         print("name error occured")
# except ZeroDivisionError:
#         print("Zero division error occured")
# finally:
#         print("finally block")

#raise----------
# try:
#     raise NameError
# except NameError:
#         print("Name error occured")
# finally:
#       print("finally block")
# WAP using exception handling and raise keyword to determine any person is elligible for
# vote or not,
# if not elligible raise valueError.
# age=int(input("Enter your age"))
# if age>=18:
#     print("you are elligible for vote")
# else:
#     try:
#         raise ValueError
#     except ValueError:
#         print("you are not elligible for vote")
#custom exception ==========
# class AgeError(Exception):
#     pass
# age=int(input("Enter your age"))
# if age<18:
    
#     try:
#         raise AgeError
#     except AgeError:
#         print("you are not elligible for vote")
# else:
#     print("You are elligible for vote")
# class SalaryNotinRange(Exception):
#     pass
# salary=int(input("Enter the salary"))
# name=input("Enter the name")
# if salary<20000 or salary>50000:
#     try:
#         raise SalaryNotinRange
#     except SalaryNotinRange:
#         print(name
              
#               )
#         print("salary not in range")
# else:
#     print("salary is in range")
    

def getAge(age):
    assert age>0,"Age can't be negative!"
    print("ok your age is:",age)
getAge(-1)