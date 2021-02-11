try:  
    x = input('Enter rainbow color:\n')
    colors = ['red', 'orange', 'yellow', 
    'green', 'blue', 'dark blue', 
    'violete']
    x_int = colors.index(x)
    if x in colors:
        if x == colors[0]:
            print('No color befor','\nColor after is', colors[1])
        elif x == colors[6]:
            print('Color before is', colors[5], '\nNo color after')
        else:
            print('Color before is', colors[x_int- 1], '\nColor after is', colors[x_int+1])
except:
    print('Enter another color')