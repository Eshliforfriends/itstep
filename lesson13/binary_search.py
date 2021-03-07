def find_bin(list, argument):
    list.sort()
    low = 0
    high = len(list) - 1
    index = None
    while low <= high and index == None:
        mid = (low + high)//2
        if argument == list[mid]:
            index = mid
        else:
            if argument < list[mid]:
                high = mid -1
            else:
                low = mid +1
    return index


list = [4,7,3,55,89,11,342,3,2,10]
print(find_bin(list, 11))
