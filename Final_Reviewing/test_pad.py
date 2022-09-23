from time import time
def counter4(n, count):
    if n == 0:
        return count
    else:
        return counter4(n - 1, count + 1)

print(counter4(10, 0))