my_list = [4, 30, 10, 15, 190, 8]
print(list(map(lambda num: num*num if num in range(10, 25) else None, my_list)))
