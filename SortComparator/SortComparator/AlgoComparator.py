import os
import sys
import time
import random
from BubbleSort import bubbleSort
from InsertionSort import insertionSort
from SelectionSort import selectionSort
from QuickSort import quickSort
from MergeSort import mergeSort
from HeapSort import heapsort
from MergeWorstCase import MergeWorstCase
from QuickBestCase import QuickBestCase


def generateBestCase(name, listSize):
    my_randoms = list()
    if name == "Bubble Sort" or name == "Insertion Sort":
        # list that is sorted
        for i in range (listSize):
            my_randoms.append(i)
    elif name == "Selection Sort":
        # does not have any different for different cases
        for i in range (listSize):
            my_randoms.append(listSize - i)
    elif name == "Quick Sort":
        my_randoms = QuickBestCase(listSize)
    elif name == "Merge Sort":
        # Both increasing and decreasing order will lead to best case in merge sort
        for i in range (listSize):
            my_randoms.append(i) 
    elif name == "Heap Sort":
        # does not have any different for different cases (theoretically)
        for i in range (listSize):
            my_randoms.append(listSize - i)
    return my_randoms

def generateWorstCase(name, listSize):
    my_randoms = list()
    if name == "Bubble Sort" or name == "Insertion Sort":
        # sorted list with reverse order
        for i in range (listSize):
            my_randoms.append(listSize - i)
    elif name == "Selection Sort":
        # does not have any different for different cases
        for i in range (listSize):
            my_randoms.append(listSize - i)
    elif name == "Quick Sort":
        # list that is sorted
        for i in range (listSize):
            my_randoms.append(i)
    elif name == "Merge Sort":
        my_randoms = MergeWorstCase(listSize)
    elif name == "Heap Sort":
        # does not have any different for different cases (theoretically)
        for i in range (listSize):
            my_randoms.append(i)
    return my_randoms


def getList(name, listSize, case):
    
    if case == 1:
        my_randoms = generateBestCase(name, listSize)
    elif case == 2:
        my_randoms = list()
        for i in range (listSize):
            my_randoms.append(random.randrange(1, 101, 1))
    elif case == 3:
        my_randoms = generateWorstCase(name, listSize)
    return my_randoms


def checkRange(num, minimum, maximum):
    """
    Do not use minimum and maximum smaller than 0 calling this function
    """
    if maximum != -1 and minimum != -1:
        if num >= minimum and num <= maximum:
            return True
        else:
            print("\tError: wrong range, choose only " + str(minimum)
                  + "~" + str(maximum) + ", please try again")
            return False
    elif maximum != -1:
        if num <= maximum:
            return True
        else:
            print("\tError: wrong range, choose only integer smaller than" +
                  str(maximum + 1) + ", please try again")
            return False
    else:
        if num >= minimum:
            return True
        else:
            print("\tError: wrong range, choose only integer larger than " +
                  str(minimum - 1) + ", please try again")
            return False 


def checkInput(question, minimum, maximum):
    """
    # using recursion
    try:
        num = int(input(question))
        if checkRange(num, minimum, maximum):
            pass
        else:
            num = checkInput(question, minimum, maximum)
    except Exception:
        print("\tError: wrong input, only integer is acceptable, please try again")
        num = checkInput(question, minimum, maximum)
    return num
    """
    while True:
        try:
            num = int(input(question))
            if checkRange(num, minimum, maximum):
                return num
        except Exception:
            print("\tError: wrong input, only integer is acceptable, please try again")


def runAlgo(name, listSize, case):
    """
    This function will run the corresponding algorithm and record
    the running time of the algorithm.
    Argument:
        name: name of the algorithm chosen
        listSize: an integer which indicate the size of list inquired
    """
    my_randoms = getList(name, listSize, case)
    start = time.time()
    if name == "Bubble Sort":
        bubbleSort(my_randoms)
    elif name == "Insertion Sort":
        insertionSort(my_randoms)
    elif name == "Selection Sort":
        selectionSort(my_randoms)
    elif name == "Quick Sort":
        quickSort(my_randoms)
    elif name == "Merge Sort":
        mergeSort(my_randoms)
    elif name == "Heap Sort":
        heapsort(my_randoms)    
    end = time.time()
    timeUse = end - start
    return timeUse

def printHistogram(algoNameList, timeList):
    """
    This function will show all the actual running time of the
    corresponding algorithms in second and display a histogram by ratio
    with maximum length of 50 (can be modified) and minimum length 0.
    Argument:
        algoNameList: name of algorithm chosen
        timeList: list of running time corresponding to the algorithm
                  (with same index)
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    maxLen = 50
    maxTime = max(timeList)
    print("Running time in second:\n")
    for i in range(len(algoNameList)):
        print(algoNameList[i]+ "\t--> " + str(timeList[i]) + " s")
    
    print("\nHistogram: Time VS Algorithm\n")
    for i in range(len(algoNameList)):
        print(algoNameList[i] + "\t" + "*" * int(timeList[i] / maxTime * maxLen))


def testing():
    # test all algorithm in each case
    algoList = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort",
                    "Merge Sort", "Heap Sort"]
    # histogram for all algorithm in best case
    print('-' * 50)
    print("Best case\n\n")
    timeList = list()
    for algo in algoList:
        timeList.append(runAlgo(algo, 990, 1))
    printHistogram(algoList, timeList)
    # histogram for all algorithm in average case
    print('-' * 50)
    print("Average case\n\n")
    timeList = list()
    for algo in algoList:
        timeList.append(runAlgo(algo, 990, 2))
    printHistogram(algoList, timeList)
    # histogram for all algorithm in worst case
    print('-' * 50)
    print("Worst case\n\n")
    timeList = list()
    """
    Do not use size larger than 990 otherwise quick sort would need too many recusion
    and the program may crash
    """
    for algo in algoList:
        timeList.append(runAlgo(algo, 990, 3))
    printHistogram(algoList, timeList)
    print('-' * 50)

def main():
    # this list will set the name of the algorithm and it is use to determine which algorithm
    algoNameList = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort",
                    "Merge Sort", "Heap Sort"]
    print("Select algorithm(s) to compare\n")
    
    # print list of existing algorithms' name
    index = 1
    for a in algoNameList:
        print(str(index) + ". " + a)
        index += 1

    print("")

    # get number of comparison
    num = checkInput("How many algorithm(s) do you want to compare: ", 1, len(algoNameList))
    
    # choose different case
    print("\n1. Best case\n2. Average case\n3. Worst case\n")
    case = checkInput("Which case do you want to implement: ", 1, 3)

    print("")

    # choose algorithm to be implemented
    algoList = list()
    for i in range(num):
        choice = checkInput("Which algorithm (by algorithm's index) [" + str(num - i) + " left]: ", 1, len(algoNameList))
        algoList.append(algoNameList[choice - 1])
    listSize = checkInput("\nWhat size of list do you want to implement: ", 1, -1)

    # run and print histogram
    print("Running . . .")
    timeList = list()
    for algo in algoList:
        timeList.append(runAlgo(algo, listSize, case))
    printHistogram(algoList, timeList)

#testing()
main()
