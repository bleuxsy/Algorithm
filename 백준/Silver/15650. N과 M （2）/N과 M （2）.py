def back(start):
    if len(grid) == M:
        print(*grid)
        return

    for i in range(start, N + 1):
        grid.append(i)
        back(i + 1)
        grid.pop()

N, M = map(int, input().split())
grid = []
back(1)