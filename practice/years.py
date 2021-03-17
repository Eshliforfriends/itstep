with open("next_generation.txt", "w") as f:
    count = 0
    for_file = []
    for n in range(2000, 2043):
        if count %10 ==0 and count != 0:
            for_file += str(n) + "\n"
            count+=1
        else:
            for_file += str(n) + " "
            count +=1
    f.writelines(for_file)


