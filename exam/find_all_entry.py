def find_all_entry(text, symbol):
    index_list = []
    for i, elem in enumerate(text):
        if elem == symbol:
            x = text.index(i)
            index_list +=  x
            return index_list

text = ['v', 55, 'f', 6, 7, 9]
symbol = 55
print(find_all_entry(text, symbol))