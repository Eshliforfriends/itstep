num = input()
try:
    type(num) == int
    x = int(num)
except ValueError:
    print('Wrong input')