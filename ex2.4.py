import json
import timeit
import matplotlib.pyplot as plt
import threading
threading.stack_size(33554432)
import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2DataSet.json") as f:
    data = json.load(f)

sizeList = []
timeList = []


for i, j in enumerate(data):
    sizeList.append(len(j))
    timeList.append(timeit.timeit(lambda:func1(j, 0, len(j)-1),number = 10))

plt.plot(sizeList, timeList, 'o-')
plt.xlabel("Input Size")
plt.ylabel("Sorting Time (s)")
plt.title("Tiime Complexity Plot")
plt.show()