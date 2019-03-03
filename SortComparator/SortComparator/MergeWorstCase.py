def separate(my_list):
    if len(my_list) <= 1:
        return my_list
    if len(my_list) == 2:
        temp = my_list[0]
        my_list[0] = my_list[1]
        my_list[1] = temp
        return my_list

    m = int(len(my_list) + 1 / 2)
    left = list()
    right = list()
    for i in range(0, len(my_list), 2):
        left.append(my_list[i])
    for i in range(1, len(my_list), 2):
        right.append(my_list[i])
    left = separate(left)
    right = separate(right)
    my_list = left + right
    return my_list

def MergeWorstCase(listSize):
    my_list = list()
    for i in range(listSize):
        my_list.append(i)
    my_list = separate(my_list)
    return my_list

"""my_list = list()
my_list = MergeWorstCase(8)
print(my_list)"""
