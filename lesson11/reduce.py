from functools import reduce
num_list = [4, -5, 78, 12, -8, 5]

multiplied_num = reduce(lambda a, b: a*b, num_list)

print(multiplied_num)