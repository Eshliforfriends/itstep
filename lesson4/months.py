try:
    x = int(input('Enter month number: '))
    months = ['January', 'February', 'March', 
            'April', 'May', 'June', 
            'July', 'August', 'September', 
            'October', 'November', 'December']
    if 1 <= x <= 12:
        print(months[x-1])
    else:
        print('Repeat with integer number from 1 to 12')
except:
    print('Repeat with integer number')
