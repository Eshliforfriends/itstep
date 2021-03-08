def unique(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    tup4 = ()
    for i in tup1:
        if i not in tup2 and i not in tup3:
            tup4 = tup4 + (i,)
    for j in tup2:
        if j not in tup1 and j not in tup3:
            tup4 = tup4 + (j,)
    for h in tup3:
        if h not in tup1 and h not in tup2:
            tup4 = tup4 + (h,)
    return tup4

tup1 = (4, 2, 6, 7)
tup2= (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)
print(unique(tup1, tup2, tup3))