import sys
# age = int(input("What is your age? : "))
while True:
    try:
        age = int(input("What is your age? : "))
        if age < 1:
            age = int(input("Input a valid age please enter a new one: "))
        if age > 1:
            new_age = age + 100
            print("Your age in 100 years is: ",new_age)
    except KeyboardInterrupt:
        sys.exit(0)

