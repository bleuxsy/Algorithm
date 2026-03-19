def printResult():

    for j in range(N):
        for i in range(N):
            if F[j][i] == 'M':
                F[j][i] = 4
            elif F[j][i] == "C":
                F[j][i] = 5
            else:
                F[j][i] = 6
    print("신봉하는 음식")
    for f in F:
        print(*f)

    print("신앙심")
    for b in B:
        print(*b)

N , T = map(int, input().split())
F = list(list(input()) for _ in range(N))
B = list(map(int, input().split()) for _ in range(N))

printResult()


