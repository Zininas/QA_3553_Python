text1 = "I want to say \"Hi\""
print(text1)
text2 = "First string\nSecond string\nThird string"
print(text2)
print(len(text1))
print(len(text2))
first_name = "Alex"
last_name = "Zinin"
full_name = first_name + " " + last_name
print(full_name)
long_string = "Xx "*5
print(long_string)
city = 'Haifa'
temperature = 27
text = f"Today in {city} the temperature is {temperature} now."
print(text)
print(f"Tomorrow will be: {temperature + 4}.")
print(f"Name is uppercase: {first_name.upper()}.")
word = "Hello"
print(word[0])
print(word[3])
print(word[-1])
print(word[0:4])
print(word[2:-1])
print(word[:2])
print(word[::-1])
example_text = ' I like walking '
print(example_text.upper())
print(example_text.lower())
print("example_text".capitalize())
print("example_text".title())
print(example_text.strip())
print(example_text.lstrip())
print(example_text.rstrip())
print(example_text.strip().replace('walking', 'hiking'))

parts = example_text.split()
print(parts)
print(" ,".join(parts))
print(example_text.find('walking'))
print("mamamamama".count("a"))
print('1234'.isdigit())
print('wert'.isalpha())
raw = ' Today is a good day '
print(raw.strip().replace(' ','*'))
date_str = "09.07.2026"
parts = date_str.strip().split(".")
print(f"Day: {parts[0]}, Month: {parts[1]}, Year: {parts[2]}")