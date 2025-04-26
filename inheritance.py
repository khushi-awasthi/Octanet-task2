# class Bank:
#     def __init__(self,interest_rate):
#         self.interest_rate=interest_rate
#     def display_interest_rate(self):
#         print("Interest_rate",self.interest_rate)
# class SBI(Bank):
#     def __init__(self):
#         # super().__init__(5)
#         Bank.__init__(self,5
#                       )
#         print("Hello")
#     def User_Detail(self):
#         self.username="Khushi"
#         print("username",self.username)
#         print("Interest_rate",self.interest_rate)
# obj_sbi=SBI()
# obj_sbi.display_interest_rate()
# obj_sbi.User_Detail()


# class Addition:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def display(self):
#         print("num1",self.num1)
#         print("num1",self.num2)
# class Addition1(Addition):
#     def add_number(self):
#         return (self.num1+self.num2)
# obj_addition=Addition1(2,3)
# obj_addition.display()
# r=obj_addition.add_number()
# print("addition is",r)


# multilevel inheritance
# class A:
#     def __init__(self):
#         print("inside the instructor")
#     def f1(self):
#         print("Super class method")
# class B(A):
#     def __init__(self):
#         print("inside the class constructor")
#         # super().__init__()
#     def f2(self):
#         print("first subclass method")
# class C(B):
#     def f3(self):
#         print("2nd sub class method")
# class D(C):
#     def f4(self):
#         print("3rd sub class method")
# d1=D()
# d1.f1()
# d1.f2()
# d1.f3()
# d1.f4()

# hierarchical inheritance
# class Animal:
#     def a(self):
#         print("Base class")
# class Bear(Animal):
#     def b(self):
#         print("Himanshu")
# class Elephant(Animal):
#     def c(self):
#         print("Kashish")
# class goat(Animal):
#     def d(self):
#         print("AB")
# d1=Bear()
# d1.b()
# d2=Elephant()
# d2.c()
# d3=goat()
# d3.d()
# //////////////////////////////////////////////////////////////
# class Employee:
#     def __init__(self,empid,ename,sal,loc,desig):
#         self.eid=empid
#         self.ename=ename
#         self.sal=sal
#         self.loc=loc
#         self.desig=desig
#     def show_details(self):
#         return self.eid+ ":" + self.ename + ":" +str(self.sal)+ ":" + self.loc + ":" + self.desig
# class Faculty(Employee):
#     def __init__(self, empid, ename, sal, loc, desig):
#         super().__init__(empid, ename, sal, loc, desig)
#         self.nol=nol

#     def show_details(self):
#         return super().show_details() + ":" + str(self.nol)
# empid="E123"
# ename="james"
# sal=24567
# loc="kanpur"
# desig="Faculty"

# if desig=="Faculty":
#     nol=25

#     fac=Faculty(empid,ename,sal,loc,desig,nol)
#     print(fac.show_details())

# if desig=="HOD":
#     bof=35

#     hod=HOD(empid,ename,sal,loc,desig,nol)
#     print(hod.show_details())

# fac
# =======================================================================
# multiple -------------
# class Calculation:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

# method overriding-----------
# class Parent:
#     def f1(self):
#         print("i am method of parent class")
# class child(Parent):
#     def f1(self):
#         print("I am method of child class")

# obj=child()
# obj.f1()
# diamond problrm---------------------
# class A:
#     def rk(self):
#         print("In class A")
# class B(A):
#     def rk(self):
#         print("In class B")
# class C(A):
#     def rk(self):
#         print("In class C")
# class D(C,B):
#     pass
# r=D()
# r.rk()
# # print(D.__mro__)
# print(D.mro())

# MRO-----------------
class A:
    def method(self):
        print("A.method() called")
class B:
    def method(self):
        print("B.method() called")
class C(A,B):
    pass
class D(C,B):
    pass
d=D()
d.method()
print(D.__mro__

)