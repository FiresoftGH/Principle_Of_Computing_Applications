import random
def makeArray():
    array = []
    for i in range(4):
            array.append(random.randint(0, 100))
    return array

print(makeArray()) 