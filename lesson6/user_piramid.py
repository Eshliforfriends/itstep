
try:
    user_rows = int(input('Enter number of rows: '))
    if user_rows > 0:
        for n in range(0, user_rows):
            print((user_rows - n)*" "+ 2* n *"*")
    else:
        print('Enter positive integer number')
except:
    print('Enter integer number')