def get_next_multiple(num):
    for n in range(1, 10000):
        yield print(num * n)

gen_multiple_of_two = get_next_multiple(2)
next(gen_multiple_of_two)
next(gen_multiple_of_two)
next(gen_multiple_of_two)
next(gen_multiple_of_two)

gen_multiple_of_thirteen = get_next_multiple(13)
next(gen_multiple_of_thirteen)
next(gen_multiple_of_thirteen)
next(gen_multiple_of_thirteen)
next(gen_multiple_of_thirteen)

