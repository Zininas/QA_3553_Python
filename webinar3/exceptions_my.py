#print('Start')
# x = 100/0    ZeroDivisionError
#print('End')

# price = int("price")  ValueError

#a = "1" + 5   TypeError

name = ["Sveta", "Misha"]
#print(name[3])   IndexError

person = {'name':"Sveta"}
#print(person['female']) KeyError

#open("nothing.txt") FileNotFoundError

try:
    x = 100 / 0
    print("res: ", x)
except ZeroDivisionError:
    print("error")

print("End")


def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("error: can`t divide by zero")
    except TypeError:
        print("error: can`t divide no digit")

print(safe_divide(4, 2))
#safe_divide(5, 0)
safe_divide(4, "two")
#==================================
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(e)
    print(type(e))

#==================================
for value in ["10", "two", 0]:
    try:
        print("100/", value, " = ", 100 / int(value))
    except (IndexError, ValueError, ZeroDivisionError) as e:
        print(e)
#==================================

try:
    person = {'name': "Sveta"}
    print(person['female'])
except KeyError:
    print("error")
except Exception:
    print("any error")
finally:
    print("finally always working")

#==================================
try:
    number = int('34')
except (TypeError, ValueError) as e:
    print(e)
else:
    print("no error", number)
finally:
    print("finally always working")

#==================================
text = "8.56"
try:
    number = float(text)
    print(number)
except (TypeError, ValueError) as e:
    print("It's not a number", e)

#==================================
student = {"name": "Ivan", "age": 20}
try:
    print(student["grade"])
except KeyError:
    print("Key not found")


#==================================
student = {"name": "Ivan", "age": 20}
try:
    print(student["age"])
except KeyError:
    print("Key not found")
finally:
    print("finally always working")

#==================================
inputs = ["12", "ноль", "0", "8"]
for value in inputs:
    try:
        result = 100 / int(value)
        print(f"100 /{value} = {result:.2f}")
    except (IndexError, ValueError, ZeroDivisionError) as e:
        print(e)