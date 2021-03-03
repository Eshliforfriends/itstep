def find_all_entry(text, symbol):
    index_list = []
    for i in text:
        if i == symbol:
            index_i = text.index(i)
            return index_i

text = ['v', 55, 'f', 6, 7, 9]
symbol = 55
print(find_all_entry(text, symbol))