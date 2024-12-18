# var1="I am a global variable"
# def my_function():
#     var2="LOcal variable"
#     print(var2)
# my_function()
# print(var1)

#local& global variable
# var1=5
# def display():
#     var2=6
#     print(var2)

# display()
# print(var1)

# global statement
# var1="I am a global variable"
# def my_function():
#     global var2
#     var2="I am also global variable"
# my_function()
# print(var1)
# print(var2)
# Function arguments=======
#keyword argument==========
# def result(abc,xyz):
#     print("abc",abc)
#     print("xyz",xyz)
# result(xyz=69,abc=88)
# Default arguments====
# def info(name,cla,mail,roll_no=34):
#     print(name)
#     print(cla)
#     print(roll_no)
#     print(mail)
# info("Khushi","MCA_I_A","abc@gmail",66)
# variable length argument
# def func(name,*fav_subject):
#     print(name)
#     print(fav_subject)
# func("goransh","Maths","Python","matlab")
# # func("Richa","Art","Java","Maths")
# func("Krish","English","Android")
#Named argument or 2nd typeof keyworded argument
def fun(arg,**args):
    print(arg)
    print(args)
fun(123,one="abc",two="xyz")
