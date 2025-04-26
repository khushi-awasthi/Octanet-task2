# class Address:
#     def __init__(self,city,mobile_no):
#          self.city=city #public
#          self.__mobile_no=mobile_no #private
#          self._state="UP" #protected
# obj_add=Address("Kanpur",12345)
# print(obj_add.city)
# print(obj_add._Address__mobile_no)#name mangling
# print(obj_add._state)

# class Student:
#     def __init__(self,id1,name):
#         self.__id1=id1
#         self.name=name
#     # getter function
#     def get_id1(self):
#         return self.__id1
#     #setter function
#     def set_id1(self,data):
#         self.__id1=data
# stu1=Student(123,"abc")
# print(stu1.get_id1()) 
 
# create a class product with following members
# state=product_id(private),product name,product price
# behavior=getter and setter of product_id and display
#access private variable outside of using namemangling
#access private variable using getter
#print all the state with in display function

# class Product:
#     def __init__(self,p_id,p_name,p_price):
#         self.__p_id=p_id
#         self.p_name=p_name
#         self.p_price=p_price
#     def get_p_id(self):
#         return self.__p_id
#     def set_p_id(self,data):
#         self.__p_id=data
#     def display(self):
#         print(self.p_name)
#         print(self.p_price)
# pro1=Product(1,"pen",10)
# print(pro1.get_p_id())
# print(pro1._Product__p_id)
# pro1.display()

class Employee:
    def __init__(self,id,name,designation,basic_salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.basic_salary=basic_salary
    def HRA(self):
        h=self.basic_salary*0.2
        return self.h
    def VA(self):
        v=self.basic_salary*0.3
        return self.v 
    def N_salary(self):
        n=self.basic_salary
        return self.n
    def display(self):
        print(self.id)
        print(self.name)
        print(self.designation)
        print(self.basic_salary)
        print(N_salary())
pro=Employee(1,'abc','deve',100000)
pro.display()

        

             