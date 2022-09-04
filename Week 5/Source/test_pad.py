import turtle

turtle.penup()
result = []
def stars2(n):
    if n > 0:
        answer = ""
        answer += "*"
        result.append(answer)
        print(''.join(result))
        stars2(n - 1)
    else:
        result.reverse()
        for x in range(len(result)):
            print(''.join(result))
            result.pop()

stars2(5)

turtle.mainloop()