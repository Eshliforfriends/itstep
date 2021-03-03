error = 'Please, enter integer number'
try:
    user_input = int(input('Please, enter integer number: '))
    if user_input < 100:
        print(user_input - 10)
    else:
        print(user_input - 20)
except ValueError:
    print(error)
