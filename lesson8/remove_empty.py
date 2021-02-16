list_with_strings = ['file', ' ', 'exam', 'math', ' ', ' ', 5, 'my task']
none = ' '
while none in list_with_strings:
    list_with_strings.remove(none)
print(list_with_strings)