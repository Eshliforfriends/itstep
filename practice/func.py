def main_func(a, b):
    def second_func(a,b):
        return a + b
    return second_func(a,b) + 5


print(main_func(4,8))
