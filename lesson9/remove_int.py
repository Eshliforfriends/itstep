def remove_int(values_list, num):
    while num in values_list:
        values_list == values_list.remove(num)
        new_list = values_list.copy()
    return new_list
values_list = [8, 7, 18, 8, 24, 95, 0, 24, 8]
print(remove_int(values_list, 8))
