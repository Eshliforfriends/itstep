def even_list_generate(range_start, range_end):
    even_list = []
    for num in range(range_start, range_end+1):
        if num %2 ==0:
            even_list.append(num)
    return even_list
print(even_list_generate(10,28))