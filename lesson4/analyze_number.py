try:
    ynumber = int(input('Enter integer number: '))
    if ynumber >= 0 and ynumber % 2 == 0:
        print(ynumber, 'positive even number')
    elif ynumber >= 0 and ynumber % 2 != 0:
        print(ynumber, 'positive odd number')
    elif ynumber < 0 and ynumber % 2 == 0:
        print(ynumber, 'negative even number')
    elif ynumber < 0 and ynumber % 2 != 0:
        print(ynumber, 'negative odd number')
except:
        print('Error. Enter integer number')
