def dummy(index):
    while True:
        sth = input("Enter: ")
        if sth == "b":
            print("Hello World")
            break
        else:
            index += 1
            print(index)

dummy(2)
