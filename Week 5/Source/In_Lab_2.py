import turtle
def stars1(n):
    stars = ""
    if n > 1:
        # stars = ""
        for x in range(n - 1):
            stars += "*"
        print(stars)
        stars1(n - 1)
        return
    elif n == 1:
        # stars = ""
        for x in range(n + 1):
            stars += "*"
        print(stars)
        stars1(n - 1)

stars1(5)
        