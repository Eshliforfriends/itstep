def remove_int_ext(values_list, num):
    count = 0
    while num in values_list:
        values_list == values_list.remove(num)
        count += 1
    return f'New list is {values_list},number of deleted figures is {count}'
values_list = [8, 7, 18, 8, 24, 95, 0, 24, 8]
print(remove_int_ext(values_list, 8))
