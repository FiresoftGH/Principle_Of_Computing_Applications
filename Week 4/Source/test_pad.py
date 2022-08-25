import sys
while True:
    try:
        sum = 0
        i = int(input("Number: "))
        while i > 1:
            j = i - 1
            while j >= 0:
                sum = sum + 1
                j = j - 1
            i = i / 2
        print(sum)
    except KeyboardInterrupt:
        sys.exit(0)