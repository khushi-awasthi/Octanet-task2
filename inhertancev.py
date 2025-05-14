# class Animal:
#     def speak1(self):
#         print("Animal make a sound")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# class puppy(Dog):
#     def speak2(self):
#         print("Puppy are playing")
# # a=Animal()
# d=Dog()
# p=puppy()
# d.speak1()
# d.speak()
# p.speak1()
# p.speak()
# p.speak2()

# Create a base class Student with a method display_name(). Create two derived classes SchoolStudent 
# and CollegeStudent that add their own methods like display_school() and display_college().
# class Student:
#     def display_name(self):
#         print("Name:")
# class SchoolStudent(Student):
#     def display_school(self):
#         print("school")
# class CollegeStudent(Student):
#     def display_college(self):
#         print("College")
# c=CollegeStudent()
# s=SchoolStudent()
# c.display_name()
# s.display_name()
# s.display_school()
# c.display_college()

# Create a base class LibraryItem with common attributes like title and author. 
# Create subclasses Book, Magazine, and DVD with additional properties and methods. Implement display_info() differently in each.

class LibraryItem:
    def library(self,title,author):
        self.title=title
        self.author=author
    def display_info(self):
        print(self.title,self.name)


class Book(LibraryItem):
    def book(self,name):
        self.name=name
    def display_info(self):
        print(self.name)
class Magzine(LibraryItem):
    def magzine(self,name):
        self.name
    def display_info(self):
        print(self.name)
class DVD(LibraryItem):
    def dvd(self,name):
        self.dvd
    def display_info(self):
        print(self.name)
d=DVD()
m=Magzine()
b=Book()
d.display_info()
