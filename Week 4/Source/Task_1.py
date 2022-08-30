from time import time
from scipy import stats
import sys
import matplotlib.pyplot as plot
import numpy as np

runtime_compare = []

def m01(n):
    rounds = 0
    sum = 0
    start_time = time()
    while rounds < n:
        sum = sum + 1
        rounds = rounds + 1

    print("M01")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m02(n):
    rounds = 0
    sum = 0
    start_time = time()
    while rounds < n:
        sum = sum + 1
        rounds = rounds  + 2

    print("M02")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m03(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < 1:
        round2s = 0
        while round2s < n:
            sum = sum + 1
            round2s = round2s + 1
        round1s = round1s + 1

    print("M03")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m04(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < n:
        round2s = 0
        while round2s < n:
            sum = sum + 1
            round2s = round2s + 10
        round1s = round1s + 20

    print("M04")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m05(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < n:
        sum = sum + 1
        round1s = round1s + 1
    round2s = 0
    while round2s < n:
        sum = sum + 1
        round2s = round2s + 1

    print("M05")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m06(n):
    round1s = 0
    sum = 0
    start_time = time()

    while round1s < n:
        round2s = 0
        while round2s < n:
            sum = sum + 1
            round2s = round2s + 1
        round1s = round1s + 1

    print("M06")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m07(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < n:
        round2s = 0
        while round2s < round1s:
            sum = sum + 1
            round2s = round2s + 1

    print("M07")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()


def m08(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < n:
        round2s = 0
        while round2s < 100 * round1s:
            sum = sum + 1
            round2s = round2s + 1
        round1s = round1s + 1

    print("M08")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m09(n):
    round1s = 0
    sum = 0
    start_time = time()
    while round1s < n:
        round2s = 0
        while round2s < n*n:
            round3s = 0
            while round3s < round2s:
                sum = sum + 1
                round3s = round3s + 1
            round2s = round2s + 1
        round1s = round1s + 1
    
    print("M09")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m10(n):
    rounds = 1
    sum = 0
    start_time = time()
    while rounds < n: # The problem had some mistakes
        sum = sum + 1
        rounds = rounds * 2
    
    print("M10")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m11(n):
    i = n
    sum = 0
    start_time = time()
    while i > 0:
        sum = sum + 1
        i = i / 2
    
    print("M11")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def m12(n):
    rounds = 0
    sum = 0
    start_time = time()
    while rounds < n:
        sum = sum + 1
        rounds = rounds * 10

    print("M12")
    print(sum)
    print("Run Time")
    end_time = time()
    print("--- %s seconds ---" % (end_time - start_time))
    runtime_compare.append(end_time - start_time)
    runtime_mean()

def run_function(select, number, repeat):
    if select == 1:
        for times in range(repeat):
            m01(number)
    elif select == 2:
        for times in range(repeat):
            m02(number)
    elif select == 3:
        for times in range(repeat):
            m03(number)
    elif select == 4:
        for times in range(repeat):
            m04(number)
    elif select == 5:
        for times in range(repeat):
            m05(number)
    elif select == 5:
        for times in range(repeat):
            m05(number)
    elif select == 6:
        for times in range(repeat):
            m06(number)
    elif select == 7:
        for times in range(repeat):
            m07(number)
    elif select == 8:
        for times in range(repeat):
            m08(number)
    elif select == 9:
        for times in range(repeat):
            m09(number)
    elif select == 10:
        for times in range(repeat):
            m10(number)
    elif select == 11:
        for times in range(repeat):
            m11(number)
    elif select == 12:
        for times in range(repeat):
            m12(number)

inputs = []

def runtime_plot(repeat):
    # inputs = []
    count = 0
    while count < repeat:
        count += 1
        inputs.append(count)
    
    print(inputs)
    runtime_list = []
    for index in range(len(runtime_compare)):
        if index > 0:
            total_time = runtime_compare[index] + runtime_list[index - 1]
            runtime_list.append(total_time)
        else:
            runtime_list.append(runtime_compare[0])

    xpoints = np.array(inputs)
    ypoints = np.array(runtime_list)
    plot.plot(xpoints, ypoints)
    plot.show()

    inputs.clear()
    runtime_list.clear()
    # plot.ylim(0, 10)

def runtime_mean():
    print(runtime_compare)
    print("Average Runtime ", stats.trim_mean(runtime_compare, 0.1))

choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    try:
        print("choice", choice_list)
        select = int(input("Enter one alglorithm choice: "))

        if select not in choice_list:
            print("Invalid Choice")
        else:
            number = int(input("Enter your number: "))
            repeat = int(input("How many times to repeat?: "))

            if repeat <= 0:
                print("Invalid Repeat Number")

            else:
                run_function(select, number, repeat)
                runtime_plot(repeat)
                runtime_compare.clear()
                
                

    except KeyboardInterrupt:
        sys.exit(0)
    
    except TypeError:
        sys.exit(0)