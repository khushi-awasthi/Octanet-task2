# Q1.Library Book System
# ➤ Design a class Book with attributes like title, author, and availability. Add
# methods to borrow and return books.
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True  # Initially, the book is available

#     def borrow_book(self):
#         if self.available:
#             self.available = False
#             print(f"You have successfully borrowed '{self.title}' by {self.author}.")
#         else:
#             print(f"Sorry, '{self.title}' is currently not available.")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print(f"You have successfully returned '{self.title}'.")
#         else:
#             print(f"'{self.title}' was not borrowed.")

#     def display_info(self):
#         status = "Available" if self.available else "Not Available"
#         print(f"Title: {self.title}, Author: {self.author}, Status: {status}")



# book1 = Book("1984", "George Orwell")
# book1.display_info()
# book1.borrow_book()
# book1.display_info()
# book1.return_book()
# book1.display_info()

# Q2.E-commerce Shopping Cart
# ➤ Build Item and Cart classes. The cart should have methods to add items, remove
# items, and calculate the total bill.

# class Item:
#     def __init__(self, name, price, quantity=1):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity


# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)
#         print(f"Added {item.quantity} x {item.name} to the cart.")

#     def remove_item(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f"Removed {item.name} from the cart.")
#                 return
#         print(f"Item '{item_name}' not found in the cart.")

#     def calculate_total(self):
#         total = sum(item.total_price() for item in self.items)
#         return total

#     def display_cart(self):
#         if not self.items:
#             print("Your cart is empty.")
#             return
#         print("Items in your cart:")
#         for item in self.items:
#             print(f"{item.name} - ₹{item.price} x {item.quantity} = ₹{item.total_price()}")
#         print(f"Total Bill: ₹{self.calculate_total()}")
# item1 = Item("Laptop", 50000, 1)
# item2 = Item("Mouse", 500, 2)

# cart = Cart()
# cart.add_item(item1)
# cart.add_item(item2)
# cart.display_cart()

# cart.remove_item("Mouse")
# cart.display_cart()

# Q3. Hotel Room Booking System
# ➤ Define a class Room with attributes like room_number, is_booked, and methods to
# book or vacate the room.
# class Room:
#     def __init__(self, room_number):
#         self.room_number = room_number
#         self.is_booked = False

#     def book_room(self):
#         if not self.is_booked:
#             self.is_booked = True
#             print(f"Room {self.room_number} has been successfully booked.")
#         else:
#             print(f"Room {self.room_number} is already booked.")

#     def vacate_room(self):
#         if self.is_booked:
#             self.is_booked = False
#             print(f"Room {self.room_number} has been vacated.")
#         else:
#             print(f"Room {self.room_number} is already vacant.")

#     def display_status(self):
#         status = "Booked" if self.is_booked else "Available"
#         print(f"Room {self.room_number}: {status}")
# room101 = Room(101)
# room101.display_status()

# room101.book_room()
# room101.display_status()

# room101.vacate_room()
# room101.display_status()

# Q4.Online Exam System
# ➤ Build a class Question with attributes like text, options, and correct_option.
# Include a method to check if an answer is correct.

# class Question:
#     def __init__(self, text, options, correct_option):
#         self.text = text
#         self.options = options
#         self.correct_option = correct_option  # This can be index (0,1,2,...) or letter ('A','B',...)

#     def display_question(self):
#         print(self.text)
#         for idx, option in enumerate(self.options):
#             print(f"{chr(65 + idx)}. {option}")  # A, B, C, ...

#     def check_answer(self, user_answer):
#         # Normalize input: accept letter ('A') or index (0)
#         if isinstance(user_answer, str):
#             user_answer = user_answer.upper()
#             user_index = ord(user_answer) - 65  # Convert A->0, B->1, etc.
#         else:
#             user_index = user_answer

#         if user_index == self.correct_option:
#             print("Correct!")
#             return True
#         else:
#             print("Incorrect.")
#             return False
# q1 = Question(
#     "What is the capital of France?",
#     ["Berlin", "Madrid", "Paris", "Rome"],
#     2  
# )

# q1.display_question()
# user_input = input("Enter your answer (A/B/C/D): ")
# q1.check_answer(user_input)

# Q5. Movie Ticket Booking System
# ➤ Create classes Movie and Ticket. Users should be able to book tickets, check
# availability, and cancel bookings.

# class Movie:
#     def __init__(self, title, total_seats):
#         self.title = title
#         self.total_seats = total_seats
#         self.booked_seats = 0

#     def check_availability(self):
#         return self.total_seats - self.booked_seats

#     def book_seat(self):
#         if self.check_availability() > 0:
#             self.booked_seats += 1
#             print(f"Seat booked for '{self.title}'.")
#             return True
#         else:
#             print(f"No seats available for '{self.title}'.")
#             return False

#     def cancel_seat(self):
#         if self.booked_seats > 0:
#             self.booked_seats -= 1
#             print(f"Booking cancelled for '{self.title}'.")
#         else:
#             print("No bookings to cancel.")

#     def display_status(self):
#         print(f"Movie: {self.title}, Available Seats: {self.check_availability()}")
        

# class Ticket:
#     def __init__(self, movie):
#         self.movie = movie
#         self.is_booke_
# m1 = Movie("Interstellar", 3)
# m1.display_status()




# Q6. Bank Loan Eligibility Checker
# ➤ Make a class Customer with attributes like income, age, and credit_score. Add a method
# to check loan eligibility based on some business rules.

# class Customer:
#     def __init__(self, name, income, age, credit_score):
#         self.name = name
#         self.income = income
#         self.age = age
#         self.credit_score = credit_score

#     def check_eligibility(self):
        
#         if self.age < 21:
#             print("Not eligible: Age must be 21 or above.")
#             return False
#         if self.income < 250000:
#             print("Not eligible: Income must be at least ₹2.5 lakh.")
#             return False
#         if self.credit_score < 650:
#             print("Not eligible: Credit score must be 650 or higher.")
#             return False

#         print("Eligible for loan.")
#         return True
# c1 = Customer("Alice", 300000, 25, 700)
# c1.check_eligibility()

# c2 = Customer("Bob", 150000, 22, 600)
# c2.check_eligibility()
