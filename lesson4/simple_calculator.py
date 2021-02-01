while True:
    try:
        number_1 = float(input('number 1: '))
        break
    except:
        print('Error. Enter a number')
while True:
    try:
        number_2 = float(input('number 2: '))
        break
    except:
        print('Error. Enter a number')
function = input('Function: +, -, *, /')
if function in ('+', '-', '*', '/'):
    if function == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif function == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif function == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif function == '/':
        if number_2 != 0:
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        else:
            print('Indivisible')
else:
    print('Not valid function')