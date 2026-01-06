def back(start):
    global flag
    if len(start) == len(S):
        if start == S:
            flag = 1
        return

    if start[-1] == "A":
        start.pop()
        back(start)
        start.append("A")

    if start[0] == "B" :
        start.reverse()
        start.pop()
        back(start)
        start.append("B")
        start.reverse()



S = list(input().strip())
T = list(input().strip())

flag = 0
back(T)
print(flag)
