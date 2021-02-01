try:
    x = int(input('Enter month number: '))
    months = ['January', 'February', 'March', 
    'April', 'May', 'June', 
    'July', 'August', 'September', 
    'October', 'November', 'December']
    if 1 <= x <= 12:
        print(months[x-1])
    else:
        print('You made mistake,repeat with integer numbers from 1 to 12')
except:
    print('You made mistake,repeat with integer numbers from 1 to 12')