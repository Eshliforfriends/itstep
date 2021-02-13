x = range(0, 11)
error = "Input must be number from 1 to 10"
try:
    user_number = int(input("Please enter a number from 1 to 10: "))
    for y in x:
        if user_number in x:
            print(user_number,'*', y ,'=', user_number * y)
        else:
            print(error)
            break
except:
    print(error)
