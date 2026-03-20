# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand



# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model


#     def info(self):
#         return f"{self.brand} is {self.model}"

    
# car1 = Car("Bmw", "X5")
# print(car1.info())


# class Father:
#     def skill(self):
#         return "Father: Driving"

# class Mother:
#     def skill(self):
#         return "Mother: Cooking"

# class Child(Father, Mother):
#     def skill(self):
#         return "Child: Coding"

# child1 = Child()
# print(child1.skill())


# class A:
#     def show(self):
#         print("A")


# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()

# d = D()
# d.show()

# print(D.__mro__)


# class Book:
#     def __init__(self, pages):
#         self.pages = pages


#     def __len__(self):
#         return self.pages


# book1 = Book(100)
# print(len(book1))

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# n1 = Number(10)
# n2 = Number(20)
# print(n1 + n2)

# class BankAccaunt:
#     def __init__(self, balanse):
#         self.balanse = balanse


#     def __add__(self, one):
#         return self.balanse + one.balanse

# b1 = BankAccaunt(100)
# b2 = BankAccaunt(200)
# print(b1 + b2)


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} added. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money!")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdraw. Balance: {self.balance}")
#     def __str__(self):
#         return f"{self.owner}'s balance: {self.balance}"


# acc1 = BankAccount("Ali", 100)

# acc1.deposit(50)
# acc1.withdraw(30)
# print(acc1)



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"{self.name} is {self.age} old"

    
# student1 = Student("Ali", 20)
# print(student1.info())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal sound"


# class Cat(Animal):
#     # shu yerga yoz
#     def speak(self):
#         return "says woof"


# cat1 = Cat("Murka")

# print(cat1.name)
# print(cat1.speak())