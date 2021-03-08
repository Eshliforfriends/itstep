def intersect(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    tup4 = ()
    for i in tup1:
        if i in tup2 and i in tup3:
            tup4 = tup4 + (i,)
    return tup4

tup1 = (4, 2, 6, 7)
tup2= (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)
print(intersect(tup1, tup2, tup3))