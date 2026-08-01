class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

fruit1 = Fruit("Apple", 100)
fruit2 = Fruit("Banana", 200)

print(fruit1.name, fruit1.weight)
print(fruit2.name, fruit2.weight)

fruit1.weight = 160
print(fruit1.name, fruit1.weight)

class Fruit1:
    def __init__(self, name, days_ripe):
        self.name = name
        self.days_ripe = days_ripe

    def describe(self):
        print(f"This is a {self.name}")

    def __str__(self):
        return f"This is a {self.name}"

    def wait_a_day(self):
        self.days_ripe -= 1
        print(f"До созревания {self.name} осталось {self.days_ripe}")

    def is_ripe(self):
        return self.days_ripe <= 0

apple = Fruit1("Apple", 2)
apple.describe()
apple.wait_a_day()
apple.wait_a_day()
print(apple.is_ripe())
print(apple)

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

c1 = Circle(2)
c2= Circle(5)
print("Area1: ", c1.area())
print("Area2: ", c2.area())
print("Pi:", Circle.pi)

class BankAccount:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance -= amount
            print(f"Снято {amount}. Balance: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено на {amount}. Balance: {self.__balance}")
        else:
            print("Cумма должна быть больше нуля")

    def get_balance(self):
        return self.__balance


account1 = BankAccount("Sveta", 1000)
account1.deposit(100)
account1.withdraw(1000)
account1.withdraw(1000)
print("Balance: ", account1.get_balance())
#print(account1.__balance)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return (f"Я {self.name}, мне {self.age} лет, "
                f"моя зарплата {self.salary}")

employee1 = Employee("John", 25, 5000)
print(employee1)

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
    def show(self):
        print(self.value)
    def __str__(self):
        return f"value : {self.value}"

counter = Counter()
counter.show()
counter.increment()
counter.increment()
counter.show()
counter.decrement()
counter.show()
print(counter)

class Thermometer:
    def __init__(self):
        self.__celsius = -273
    def set_temp(self, t):
        if t < -273:
           print("Error")
        else:
            self.__celsius = t
            print(f"Temperature: {self.__celsius}")
    def get_temp(self):
        return self.__celsius
t1 = Thermometer()
print(t1.get_temp())
t1.set_temp(-275)
print(t1.get_temp())
t1.set_temp(50)
print(t1.get_temp())