def my_function(list):
    result = 0
    if list[1] + list[2] == list[-1]:
        result += 1
    for n in list[3:]:
        result += n
    for n in list[:2]:
        result += n
    if list[1] ** 2 == list[3]:
        result += 1
    return result


print(my_function([1, 2, 3, 4]))