''' recursive problems '''

def factorial(n): # n >= 0
    if n == 0:
        return 1
    return n * factorial(n-1)

def multiple(a, b): # b บวกกัน a ครั้ง : a >= 0
    if a == 0:
        return 0
    return b + multiple(a-1, b)

def power(a, b): # b >= 0
    if b == 0:
        return 1
    return a * power(a, b-1)

def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def bubble_sort(l, n): #start n = len(l)
    if n == 1:
        return l
    for i in range(n-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    bubble_sort(l, n-1)
    return l

print(bubble_sort([7, 2, 5, 4, 5], 3))

def recaman(n, seq): #start seq = []
    if n == 1:
        seq.append(n)
        return 1
    a = recaman(n-1, seq)
    if a - n > 0 and a - n not in seq:
        seq.append(a-n)
        return a - n
    else:
        seq.append(a+n)
        return a + n

def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    if a % b == 0:
        return a
    return int(lcm(b, a % b) / (a % b) * a)

def max(l):
    if len(l) == 1:
        return l[0]
    a = l[0]
    b = max(l[1:])

    if a > int(b):
        return a
    else:
        return b

def min(l):
    if len(l) == 1:
        return l[0]
    a = l[0]
    b = min(l[1:])

    if a < int(b):
        return a
    else:
        return b

def sum(l):
    if len(l) == 1:
        return l[0]
    return l[0] + sum(l[1:])

def print_star1(n):
    if n == 0:
        return
    print('*' * n)
    print_star1(n-1)
    print('*' * n)

def print_star2(n, i): #start i = 1
    if i == n + 1:
        return
    print('*' * i)
    print_star2(n, i+1)
    print('*' * i)

def binary_search(l, n): #(sorted list, num) => return index of n in l
    mid = len(l) // 2
    if l[mid] == n:
        return mid
    if len(l) == 1:
        return None
    if l[mid] < n and binary_search(l[mid:], n) is not None:
        return mid + binary_search(l[mid:], n)
    return binary_search(l[:mid], n)
