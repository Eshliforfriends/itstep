code = ['a', 'b', 'c', 'd',
     'e', 'f', 'g', 'h',
     'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p',
     'q', 'r', 's', 't',
     'u', 'v', 'w', 'x',
     'y', 'z']
code_up = ['A', 'B', 'C', 'D',
     'E', 'F', 'G', '`H`',
     'I', 'J', 'K', 'L',
     'M', 'N', 'O', 'P',
     'G', 'R', 'S', 'T',
     'U', 'V', 'W', 'X',
     'Y', 'Z']
user_input = input('Enter something: \n')
count = 0
new_str =''

for i in user_input:
    if i in code[0:13]:
        user_input = user_input.replace(i, code[code.index(i)+13])
        new_str += user_input[count]
        count += 1
    elif i in code[13:27]:
        user_input = user_input.replace(i, code[code.index(i)-13])
        new_str += user_input[count]
        count += 1
    elif i in code_up[0:13]:
        user_input = user_input.replace(i, code_up[code_up.index(i) + 13])
        new_str += user_input[count]
        count += 1
    elif i in code_up[13:27]:
        user_input = user_input.replace(i, code_up[code_up.index(i) - 13])
        new_str += user_input[count]
        count += 1
        continue
print(new_str)

