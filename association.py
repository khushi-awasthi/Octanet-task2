# class customer:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def details(self):
#         print("Her name is",self.name)
#         print("Address")
#         print(self.address.street)
#         print(self.address.city)
# class Address:
#     def __init__(self,street,city):
#         self.street=street
#         self.city=city
# add=Address("Shyam Nagar","Kanpur")
# cus=customer("Kashish",add)
# cus.details()

class college:
    def __init__(self,name,student):
        self.name=name
        self.student=student
    def details(self):
        print("name is",self.name)
        print("college")
        print(self.student.sid)
        print(self.student.course)
class student:
    def __init__(self,sid,course):
        self.sid=sid
        self.course=course

stu=student("2001","MCA")
clg=college("PSIT",stu)
clg.details()
        
        


