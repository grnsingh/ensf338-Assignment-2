import timeit
import matplotlib.pyplot as plt

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibM(n, fibonacciDict={}):
    if n in fibonacciDict:
        return fibonacciDict[n]
    elif n == 0 or n == 1:
        fibonacciDict[n] = n
    else:
        fibonacciDict[n] = fibM(n-1,fibonacciDict) + fibM(n-2, fibonacciDict)
    return fibonacciDict[n]

def main():
    fibList=[]
    fibMList=[]
    n = 36
    for i in range(n):
        fibList.append(timeit.timeit(lambda:fib(i),number = 10))
        fibMList.append(timeit.timeit(lambda:fibM(i),number = 10))


    numbersList=list(range(n))
    plt.plot(numbersList, fibList, label = "fib" )
    plt.plot(numbersList, fibMList, label="fibM")
    plt.legend()
    plt.xlabel("Numbers")
    plt.ylabel("Time(seconds)")
    plt.title("Time Complexity Plot")
    plt.show()   

main()