def only_odd_arguments(func):
    def wrapper_odd(*args):
        n = 1
        for i in args:
            for j in args:
                if j % 2 != 0:
                    if n < len(args):
                        n += 1
                        continue
                    elif n == len(args):
                        return print(func(*args))
                else:
                    print('Enter odd arguments')
                    break
            break
    return wrapper_odd

@only_odd_arguments
def add(a, b):
   return a + b

add(4, 4)
add(5, 5)

@only_odd_arguments
def multiple(a, b, c, d, e):
   return a*b*c*d*e

multiple(11,7,8,1,5)
multiple(5,5,11,9,5)
