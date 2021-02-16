list_with_strings = ['file', '', 'exam', 'math', ' ', ' ', 5, 'my task']
new_list = []
for i in list_with_strings:
    if str(i).isspace() or not i:
        # list_with_strings.remove(none)
        continue
    else:
        new_list.append(i)
print(new_list)
