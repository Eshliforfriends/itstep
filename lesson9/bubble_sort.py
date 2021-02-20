def bubble_sort(num_list, reverse= False):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n-1):
            if reverse == False:
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            else:
                if num_list[j] < num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return bubble_sort
num_list = [6,1, 45, 3, 7,15,0]
bubble_sort(num_list, True)
print(num_list)