def only_odd_arguments(func):
    def wrapper_odd(*args):
        n = 0
        for i in args:
            if i % 2 != 0:
                if n <= len(args):
                    n +=1
                    print(n)
                    continue
                else:
                    print(func(*args))
            else:
                print('Please enter odd numbers')
                break
    return wrapper_odd

@only_odd_arguments
def add(a, b):
   return a + b

# add(4, 4)
add(5, 5)
#
# @only_odd_arguments
# def multiple(a, b, c, d, e):
#    return a*b*c*d*e

# multiple(4*2*7*1*5)
# multiple(7*3*11*9*3)