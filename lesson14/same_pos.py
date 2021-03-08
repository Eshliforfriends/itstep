def same_pos(tup1: tuple, tup2: tuple, tup3: tuple) -> dict:
    dict_new = {}
    for i, elem in enumerate(tup1):
        if tup1[i] == tup2[i] == tup3[i]:
            dict_new[i] = elem
    return dict_new


tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 7)
tup3 = (2, 2, 2, 7, 1)
print(same_pos(tup1, tup2, tup3))