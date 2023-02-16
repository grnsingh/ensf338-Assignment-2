def fibM(n, fibonacciDict={}):
    if n in fibonacciDict:
        return fibonacciDict[n]
    elif n == 0 or n == 1:
        fibonacciDict[n] = n
    else:
        fibonacciDict[n] = fibM(n-1,fibonacciDict) + fibM(n-2, fibonacciDict)
    return fibonacciDict[n]