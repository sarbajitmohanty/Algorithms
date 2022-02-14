# O(2^n) time | O(n) space
def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 2)


# O(n) time | O(n) space
def getNthFib2(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
        return memoize[n]


# O(n) time | O(1) space
def getNthFib3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


# O(1) time | O(1) space
import math
def fib(n):
    res = (((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n)/math.sqrt(5)
    return res

res = round(fib(1020))
res2 = math.log(res, 10)
res3 = math.floor(res2) + 1
print(res)
