while True:
    try:
        x = str(input('Enter rainbow color: '))
        colors = ('red', 'orange', 'yellow', 
        'green', 'blue', 'dark blue', 
        'violete')
        break
    except:
         print('You made mistake,repeat with other color')
if x == 'red':
    print('none', colors[+1])
elif x == 'violete':
    print(colors[-1], 'none')
else:
    print(colors[-1],colors[+1])
