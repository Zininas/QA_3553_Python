person = {
    "name": "Alex",
    "age": 40,
    "city": "Haifa"
}
print(person)

empty_dict = {}
print(empty_dict)

print("Count of keys: ", len(person))
print("Count of values: ", len(person))

print(person["name"])
print(person["age"])
print(person["city"])

print(person.get("cita"))
print(person.get("cita", "Not found"))

person["phone"] = '053540444'
print(person)

person["age"] = 41
person.update({"phone": "55435445"})
print(person)

del person["age"]
print(person)
del person["city"]
print(person)
print("name" in person)
print("email" in person)

prices = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    "mango": 400,
}

for product in prices:
    print("Product: ", product)
    print("Price: ", prices[product])

for product, price in prices.items():
    print(f"Product: {product}, Prise: {price}")

print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))

dict_any_types = {
    1: "paz",
    "two": 2,
    (0,1): "point"
}
