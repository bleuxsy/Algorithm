def back():
    if len(grid) == M :
        print(" ".join(map(str,grid)))
        return
    for i in range(1, N+1):
        if i not in grid:
            grid.append(i)
            back()
            grid.pop()

N, M = map(int, input().split())
grid = []
back()