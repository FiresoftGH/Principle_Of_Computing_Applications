import sys

convert_dict = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I', 
'19': 'J', '20': 'K', '21 ': 'L', '22 ': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q','27': 'R', '28': 'S', '29': 'T',
'30': 'U', '31': 'V', '32': 'W', '33': 'X', '34': 'Y', '35' :'Z'}

invert_convert_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

#Number Conversion Part

def from_decimal(num,base_order):
    choice_1_ans = ""

    while num // base_order != 0:
        if num % base_order < 10:
            rem1 = str(num % base_order)
        else:
            rem1 = str(num % base_order)
            rem1 = convert_dict[rem1]
        num = num // base_order
        choice_1_ans += rem1

    # choice_1_ans = choice_1_ans + str(num % base_order)
    print(choice_1_ans[::-1])

def to_decimal(num,base_order):
    choice_2_ans = 0
    num_array = []

    for digits in num:
        num_array.append(invert_convert_dict[digits])
    
    digit = len(num_array) - 1
    index = 0

    while digit >= 0:   
        choice_2_ans += (num_array[index] * (base_order ** digit))
        digit -= 1
        index += 1
    
    if max(num_array) > base_order:
        print("Error: Incorrect Number/Base")
    else:
        print(choice_2_ans)

# User Input Part (Legacy)

# choice = int(input("Type '1' to convert decimal to other bases and '2' to convert other bases to decimal: "))

# if choice == 1:
#     num = int(input("Enter a number you desired: "))
#     base_order = int(input("Enter the base you want to convert to: "))

#     from_decimal(num,base_order)

# elif choice == 2:
#     num = str(input("Enter a number: "))
#     base_order = int(input("Enter the base number of your number: "))

#     to_decimal(num,base_order)

# User Input Part (Current)

while True:
    try:
        choice = int(input("Type '1' to convert decimal to other bases and '2' to convert other bases to decimal: "))

        if choice == 1:
            try:
                num = int(input("Enter a number you desired: "))
                base_order = int(input("Enter the base you want to convert to: "))

                if num < 0:
                    print("Error: Negative number")
                elif base_order < 0:
                    print("Error: Negative Base")
                elif base_order > 36:
                    print("Error: Base > 36")
                else:
                    from_decimal(num,base_order)
    
            except KeyboardInterrupt:
                print("Exiting...")
                sys.exit(0)

        elif choice == 2:
            try:
                num = str(input("Enter a number you desired: ")).upper()
                base_order = int(input("Enter the base number of your number: "))

                if "-" in num:
                    print("Error: Negative Number")
                elif base_order < 0:
                    print("Error: Negative Base")
                elif base_order > 36:
                    print("Error: Base > 36")
                else:
                    to_decimal(num,base_order)
            
            except KeyboardInterrupt:
                print("Exiting...")
                sys.exit(0)
                
        elif choice > 2:
            print("Error: Invalid Choice")
        
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)