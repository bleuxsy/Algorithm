def back():
    if len(grid) == M:
        print(*grid)
        return
    for i in range(1, N+1):
        grid.append(i)
        back()
        grid.pop()


N, M = map(int, input().split())
grid = []
back()