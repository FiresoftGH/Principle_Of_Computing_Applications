output = []
input1 = [1,1,2,3,5,8]

def mystery1(dummy):
    if len(dummy) == 1: # Base Case
        output.append(dummy[0])
        print("Outputs: ", output)
        return dummy[0]

    else: # Recursive Case
        a = dummy[0]
        dummy.pop(0)
        b = mystery1(dummy)

        if a > b:
            output.append(a)
            print("Outputs: ", output)
            return a
        else:
            output.append(b)
            print("Outputs: ", output)
            return b

mystery1(input1)