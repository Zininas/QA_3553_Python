class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}."

employee_1 = Employee("Anna","QA Engineer",7000)
employee_2 = Employee("Alex","IOS Developer",15000)
print(employee_1.get_info())
print(employee_2.get_info())

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def buy(self,amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            return "Not enough products"

laptop = Product("Laptop",500,5)

print(laptop.buy(2))
print("Remaining balance after purchase 2 шт.:", laptop.quantity)

print(laptop.buy(10))
print("The balance has not changed.:", laptop.quantity)

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"

vehicle = Vehicle()
car = Car()
bicycle = Bicycle()

print(vehicle.move())
print(car.move())
print(bicycle.move())

class User:
    country = "Israel"

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

user1 = User("Alex", 25)
user2 = User("Stas", 30)
user3 = User("Masha", 22)

print("--- До изменения country ---")
print(f"{user1.username}: {user1.country}")  # Israel
print(f"{user2.username}: {user2.country}")  # Israel
print(f"{user3.username}: {user3.country}")  # Israel

User.country = "Canada"

print("\n--- После изменения User.country = 'Canada' ---")
print(f"{user1.username}: {user1.country}")  # Canada
print(f"{user2.username}: {user2.country}")  # Canada
print(f"{user3.username}: {user3.country}")  # Canada
