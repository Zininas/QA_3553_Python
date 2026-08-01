# 1-9 |10-99| 100-299
import re

IS_POSITIVE_LESS_THAN_300_PATTERN = r"[1-9]|[1-9][0-9]|[1-2][0-9]{2}"
#pattern = r"^([1-9]|[1-9]\d|[12]\d{2})$"

def is_positive_less_than_300(value):
    return bool(re.fullmatch(IS_POSITIVE_LESS_THAN_300_PATTERN,value))

print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("298"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("65567g"))
print(is_positive_less_than_300("3.14"))
print()

#1-99 | 100-199 | 200-249 | 250-255

IS_NUMBER_FROM_1_TO_255_PATTERN = r"([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

def is_number_from_1_to_255(value):
    return bool(re.match(IS_NUMBER_FROM_1_TO_255_PATTERN, value))

print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2555"))
print()

IS_ISRAEL_MOBILE_PATTERN = r"(0|\+972)5[0-9](-?\d){7}"

def is_israel_mobile(phone):
    return bool(re.fullmatch(IS_ISRAEL_MOBILE_PATTERN, phone))

print(is_israel_mobile("0541234567"))
print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))
print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))
print()

#00:00 - 23:59

IS_VALID_TIME_PATTERN = r"([0-1][0-9]|2[0-3]):([0-5][0-9])$"

def is_valid_time(time):
    return bool(re.fullmatch(IS_VALID_TIME_PATTERN, time))

print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))

print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))
print()

IS_ISRAEL_CAR_NUMBER_PATTERN = r"\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3}"

def is_israel_car_number(number):
    return bool(re.fullmatch(IS_ISRAEL_CAR_NUMBER_PATTERN, number))

print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))