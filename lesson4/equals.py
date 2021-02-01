try:
    number1 = float(input('Your first number, not words!'))
    number2 = float(input('Your second number,not words!'))
    if number1 == number2:
        print('EQUALS')
    elif number1 != number2 and number1 > number2: 
        print(number1)
        print(number2)
    else:
        print(number2)
        print(number1)
except ValueError:
    print('Am I a Joke to you?')