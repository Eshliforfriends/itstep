num_list = [5, 'government', 'lesson', 234, 'responsibility', 'other', 4777732]

new_list = filter(lambda num: num if len(str(num)) >= 6 else 0, num_list)

print(list(new_list))
