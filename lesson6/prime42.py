counter = 0
for x in range(2, 999):
    if counter < 43:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print(x)
            counter += 1
