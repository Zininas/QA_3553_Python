def print_string_reverse(s):
    if s is None or s.strip() == "":
        print("Wrong string")
    else:
        print(s[::-1])

print_string_reverse("Shalom")
print_string_reverse("")
print_string_reverse("   ")
print_string_reverse(None)

def is_isr_phone_number(phone):
    if phone is None or not isinstance(phone, str) or phone.strip() == "":
        return None
    if phone.isdigit() and len(phone) == 10 and phone.startswith('0'):
        return True
    return False

print(is_isr_phone_number("0501234567"))
print(is_isr_phone_number("1501234567"))
print(is_isr_phone_number("050123456"))
print(is_isr_phone_number("050-123456"))
print(is_isr_phone_number("050123456A"))
print(is_isr_phone_number(None))
print(is_isr_phone_number(""))


def print_substring_reverse(s, start, finish):
    if s is None or not isinstance(s, str) or s.strip() == "":
        print("Wrong args")
        return
    if start < 0 or finish >= len(s) or start > finish:
        print("Wrong args")
        return
    result = s[:start] + s[start:finish + 1][::-1] + s[finish + 1:]
    print(result)

print_substring_reverse("Shalom", 1, 3)
print_substring_reverse("Shalom", 0, 5)
print_substring_reverse("Shalom", 3, 1)
print_substring_reverse("Shalom", 1, 10)
print_substring_reverse("   ", 1, 2)

def get_words_reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(get_words_reverse("Hello my nice world"))

def print_words_reverse_in_column(s):
    words = s.split()
    for word in words:
        print(word[::-1])

print_words_reverse_in_column("Hello my nice world")
