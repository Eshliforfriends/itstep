try:
    number35 = float(input('Enter a number in range from 1 to 100: '))
    if number35 <= 100 and number35 >= 1:
        if number35 % 3 == 0 and number35 % 5 == 0:
            print('FizzBuzz')
        elif number35 % 3 == 0:
            print('Fizz')
        elif number35 % 5 == 0:
            print('Buzz')
        elif number35 % 3 != 0 and number35 % 5 != 0:
            print(' ')
    else: print('Error! Enter a number in a range from 1 to 100')   
except ValueError:
    print('Error. Enter a number')