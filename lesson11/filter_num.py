num_list = [8, -7, 45, -99, 0, 345, -873, 0]

filter_num = filter(lambda num: num < 0 , num_list)

print(list(filter_num))
