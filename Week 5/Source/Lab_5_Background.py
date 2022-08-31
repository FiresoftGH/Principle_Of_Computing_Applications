# Example of a recursive function

from math import factorial

def run_fact(n):
    return factorial(n)

def fact(n):
    if n == 1:
        print(n)
    else:
        print(n * run_fact(n - 1))

# Comment out the line below to run the function and adjust its arguements
# fact(1)
# Personal Homework: write a recursive definition of the function above

# Tracing a recursive function

def mystery(n): # Dummy Alglorithm
    return n

def run_mystery(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        result = mystery(n - 1) + 1 # Even
        return result
    else:
        result = mystery(n - 1) + 2 # Odd
        return result

run_mystery(10)




