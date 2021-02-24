init_list = [['Gold','Silver'], [6, 456,  52], ['Bronz', 'Copper'], [123,0, -45]]

new_list = []

map_list = list(map(lambda elem: new_list.extend(elem), init_list))
filter_list = filter(lambda x: x if type(x) == int else None, new_list)

print(list(filter_list))
