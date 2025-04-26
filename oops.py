#  step 1:class creation 
# class circle:
#     def __init__(self,r,c):
#         self.radius=r
#         self.color=c
#     def getcolor(self):
#         print("The color is",self.color)
#     def getRadius(self):
#         print("The radius is",self.radius)
#     def getArea(self):
#         area=3.14*self.radius*self.radius
#         print("Area of circle is",area)
# # step2:object creation
# obj=circle(5,"pink")
# # step 3:accessing class member
# obj.getRadius()
# obj.getArea()
# obj.getcolor()

# class student:
    
#     def __init__(self,i,n,c):
#         self.id=i
#         self.name=n
#         self.college=c
#     def getId(self):
#         print("student id",self.id)
#     def getOther(self):
#         print("student name",self.name)
#         print("student college",self.college)
# a=int(input("enter the id"))
# b=input("enter name")
# c=input("enter college name")
        
# obj=student(a,b,c)
# obj.getId()
# obj.getOther()

# class employee:
#     def __init__(self,id):
#         self.empid=id
#     def getOffer(self):
#         if id>=9000 and id<=10000:
#             print("elligible")
# a=int(input ("enter id"))

# obj=employee(a)
# obj.getOffer()
        # ===================================
# class ABC:
#     var=10
# obj=ABC()
# print(obj.var)

# class ABC:
#     var=10
#     def display(self):
#         print("In class....")
# obj=ABC()
# print(obj.var)
# obj.display()

# class computer:
#     def __init__ (self):
#         print("In Init")
#     def config(self):
#         print("17","ITB","SGB")
# com1=computer()
# com1.config()
# com2=computer()
# com2.config()

# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print("Configuration is",self.cpu,self.ram)
# com1=computer('i5','Sgb')
# com2=computer('i7','16gb')
# com1.config()
# com2.config()

# class mine:
#     def __init__(self,name,rollno,city):
#         self.name=name
#         self.rollno=rollno
#         self.city=city
#     def display(self):
#         print("name is",self.name,"\n rollno is",self.rollno,"\n city is",self.city)
# a=mine('Khushi',2412440,'Unnao')
# a.display()

# class number:
#     def __init__(self,n1):
#         self.n1=n1
       
#     def display(self):
#         if self.n1 % 2==0:
#             print("even")
#         else:
#             print("Odd")
# a=number(2)
# a.display()

# class Emp:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#     def display(self):
#         print(self.id)
#         print(self.name)
# obj1=Emp(123,"Khushi")
# obj2=Emp(124,"Kashish")
# obj1.salary=250000
# obj1.com_name="IBM"
# obj2.designation="Developer"
# obj2.salary=250000


# print(id(obj2.salary))
# print(id(obj1.salary))
# obj1.display()

class Emp_bonus:
    def __init__(self,a):
        print("inside first constructor")
    def __init__(self):
        print("Second constructor")
    def __init__(k,m,n):
        k.m=4
        print(k.m)
obj1=Emp_bonus(5,6)


