# Tracing a recursive function

data = []
n_value = []

def mystery(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        result = mystery(n - 1) + 1 # Even
        n_value.append(n)
        data.append(result)
        print("Values of n",  n_value)
        print("Values of result", data)
        return result
    else:
        result = mystery(n - 1) + 2 # Odd
        n_value.append(n)
        data.append(result)
        print("Values of n", n_value)
        print("Values of result", data)
        return result

mystery(10)




