def print_list_reverse(my_list):
    if not isinstance(my_list,list) or my_list is None or my_list == []:
        print("Wrong list")
        return
    print(my_list[::-1])

print_list_reverse([1,2,3,4,5])
print_list_reverse((1,2,3,4,5,3,9,7))
print_list_reverse(None)
print_list_reverse([])

def is_valid_point(point):
    if point is None or point == ():
        return None
    if not isinstance(point, tuple) or len(point) != 2:
        return False
    x, y = point
    return isinstance (x,(int,float)) and isinstance (y,(int,float))

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print(is_valid_point([]))

def print_sublist_reverse(my_list, start, finish):
    if not isinstance(my_list, list) or not isinstance(start, int) or not isinstance(finish, int) or not my_list:
        print("Wrong args")
        return
    if start < 0 or finish < 0 or start >= len(my_list) or finish >= len(my_list) or start > finish:
        print("Wrong args")
        return
    result = my_list.copy()
    result[start:finish + 1] = result[start:finish + 1][::-1]
    print(result)

print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([], "0", 2)
print_sublist_reverse([1, 2, 3,4,5,6,7], 0, 2)
print_sublist_reverse([1, 2, 3,4,5,6,7], 2, 0)


def get_students_by_grade(students):
    if not isinstance(students, dict) or not students:
        return {}
    result = {}
    for name, grade in students.items():
        if grade not in result:
            result[grade] = [name]
        else:
            result[grade].append(name)

    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))