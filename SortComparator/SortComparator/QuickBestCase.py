def generate(my_list, begin, end):
    count = end - begin
    if count < 3:
        return my_list
    else:
        # Find a middle element index
        # This will be the pivot element for the part of the list [begin; end)
        middle = begin + int((count - 1) / 2)
        # Make the left part best-case first: [begin; middle)
        my_list = generate(my_list, begin, middle)
        # Swap the pivot and the start element
        temp = my_list[begin]
        my_list[begin] =  my_list[middle]
        my_list[middle] = temp
        # Make the right part best-case, too: (middle; end)
        middle += 1
        my_list = generate(my_list, middle, end)
        return my_list


def QuickBestCase(listSize):
    my_list = list()
    for i in range(listSize):
        my_list.append(i)
    my_list = generate(my_list, 0, listSize)
    return my_list

