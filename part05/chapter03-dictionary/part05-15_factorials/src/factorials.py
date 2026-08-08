import math 

def factorials(n: int):
    factorials = {}
    for i in range(1, n+1):
        factorials[i] = (math.factorial(i))
    return factorials