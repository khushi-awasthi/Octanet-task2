# # # # #exercise  on basics of function===============
# # # # #lex_auth_01269361601342668881
# # # # def calculate_total_ticket_cost(no_of_adults, no_of_children):
# # # #     total_ticket_cost=0
# # # #     #Write your logic here
# # # #     intermediate_result=(no_of_adults*37550.0 )+(no_of_children*(37550.0 /3))
# # # #     service_tax=(7/100)*intermediate_result
# # # #     intermediate_result=intermediate_result+service_tax
# # # #     discount=(10/100)*intermediate_result
# # # #     total_ticket_cost=intermediate_result-discount
    

# # # #     return total_ticket_cost


# # # # #Provide different values for no_of_adults, no_of_children and test your program
# # # # total_ticket_cost=calculate_total_ticket_cost(1,2)
# # # # print("Total Ticket Cost:",total_ticket_cost)

#  Lambda function------------------
# addition of two number using lambda function-------
# sum1=lambda num1,num2:num1+num2
# num3=sum1(34,6)
# print("Addition of two number is",num3)
# print(sum1(32,7))

# WAP  to perform cube of any number using lambda function.-----------
# cube=lambda num1:num1*num1*num1
# num2=cube(2)
# print("Cube of a number is",num2)

# LIST=======
# name=["raj","geny","shubh"]
#  print(name[1])
# print(name[-3])
 # for element in name:
  #     print(element)

# zeros=[0]*20
# print(zeros)

# n1=[5,6]
# print(n1*3)

# list=[0,1,2,3,4]
# print(list[2:4])
list1=[4,5,"raj",6.0,"a"]
# print(list1[0:3])
# list updation============
list1[2]="shubh"
print(list1)
# list deletion========
del list1[3]
print (list1)







# ====================================
#lex_auth_012693797166096384149

def find_leap_years(given_year):

    # Write your logic here
    count++
    list_of_leap_year=[]
    while(count<15):
        if((given_year%400==0 or given_year%100!=0)and given_year%==0):
            list_of_leap_year.append(given_year)
            count=count+1
        given_year=given_year+1

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
