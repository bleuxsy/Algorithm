import sys
from collections import deque
import heapq


sys.stdin = open("input.txt", "r")


def result_print(txt, lst):
    print(txt)
    for g in lst:
        print(*g)
    print("=========")

def bfs(sx, sy, visited):

    gewel = 1
    stack = deque()
    stack.append((sx, sy))
    visited[sx][sy] = True

    while stack:
        cx, cy = stack.pop()


        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx+dx, cy+dy

            if 0<= nx <5 and 0<= ny <5 and not visited[nx][ny] and grid_n[cx][cy] == grid_n[nx][ny] :
                visited[nx][ny] = True
                gewel += 1
                stack.append((nx, ny))



    if gewel >= 3:

        return gewel
    else:
        return 0

def explore(r, c):

    global grid_n
    now_grid = []
    global explore_lst

    for i in range(r-1,r+2):
        row = []
        for j in range(c-1, c+2):
            row.append(grid[i][j])
        now_grid.append(row)


    new_grid = [[0]* 3 for i in range(3)]

    # 90도 일때
    for i in range(3):
        for j in range(3):
            new_grid[j][abs(2-i)] = now_grid[i][j]
    grid_n = [g[:] for g in grid]
    # 유물 탐색
    for i in range(3):
        for j in range(3):
            grid_n[i+r-1][j+c-1] = new_grid[i][j]


    visited = [[False] * 5 for i in range(5)]
    cnt = 0

    for x in range(5):
        for y in range(5):
            if not visited[x][y]:

                cnt += bfs(x, y, visited)
    heapq.heappush(explore_lst, (-cnt, 90,c, r))





   # 180도 일때
    for i in range(3):
        for j in range(3):
            new_grid[abs(2-i)][abs(2-j)] = now_grid[i][j]
    grid_n = [g[:] for g in grid]
    for i in range(3):
        for j in range(3):
            grid_n[i+r-1][j+c-1] = new_grid[i][j]


    visited = [[False] * 5 for i in range(5)]
    cnt = 0
    for x in range(5):
        for y in range(5):
            if not visited[x][y]:

                cnt += bfs(x, y, visited)

    heapq.heappush(explore_lst, (-cnt, 180, c, r))

    # 270도 일때
    for i in range(3):
        for j in range(3):
            new_grid[abs(2-j)][i] = now_grid[i][j]
    grid_n = [g[:] for g in grid]
    for i in range(3):
        for j in range(3):
            grid_n[i + r - 1][j + c - 1] = new_grid[i][j]


    visited = [[False] * 5 for i in range(5)]
    cnt = 0
    for x in range(5):
        for y in range(5):
            if not visited[x][y]:

                cnt += bfs(x, y, visited)
    heapq.heappush(explore_lst, (-cnt, 270, c, r))



    return
def erase_jewel(sx, sy, visited):
    stack = deque()
    stack.append((sx, sy))
    visited[sx][sy] = True
    jewels = [(sx, sy)]

    while stack:
        cx, cy = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and grid_n[cx][cy] == grid_n[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                jewels.append((nx, ny))

    if len(jewels) >= 3:
        return jewels
    return []

def erase_grid():
    global erase, grid_n
    global total
    total += len(erase)
    erase.sort(key= lambda x: (x[1], -x[0]))

    while erase:
        sx, sy = erase.pop(0)
        num = wall.pop(0)
        grid_n[sx][sy] = num






    return [g[:] for g in grid_n]

def make_grid(rd, r, c):
    global grid_n


    new_grid = [[0] * 3 for i in range(3)]
    now_grid = []

    for i in range(r - 1, r + 2):
        row = []
        for j in range(c - 1, c + 2):
            row.append(grid[i][j])
        now_grid.append(row)

    grid_n = [g[:] for g in grid]
    if rd == 90:
        for i in range(3):
            for j in range(3):
                new_grid[j][abs(2 - i)] = now_grid[i][j]

        # 유물 탐색
        for i in range(3):
            for j in range(3):
                grid_n[i + r - 1][j + c - 1] = new_grid[i][j]


    elif rd == 180:
        for i in range(3):
            for j in range(3):
                new_grid[abs(2 - i)][abs(2 - j)] = now_grid[i][j]

        for i in range(3):
            for j in range(3):
                grid_n[i + r - 1][j + c - 1] = new_grid[i][j]


    else:
        for i in range(3):
            for j in range(3):
                new_grid[abs(2 - j)][i] = now_grid[i][j]
        grid_n = [g[:] for g in grid]
        for i in range(3):
            for j in range(3):
                grid_n[i + r - 1][j + c - 1] = new_grid[i][j]

    return
def addjewel():
    global grid_n
    global erase

    erase = []
    visited = [[False] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:

                erase.extend(erase_jewel(i, j, visited))


    return

if __name__ == "__main__":
    explore_lst = []
    K, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(5)]
    wall = list(map(int, input().split()))
    answer = []
    for _ in range(K):
        erase = []
        total = 0
        explore_lst = []
        grid_n = [g[:] for g in grid]
        for i in range(1, 4):
            for j in range(1, 4):
                explore(i, j)
        _, max_rd, max_y, max_x = heapq.heappop(explore_lst)

        make_grid(max_rd, max_x, max_y)
        while True:
            addjewel()
            if not erase:

                break
            grid = erase_grid()


        if total > 0:
            answer.append(total)


    print(*answer)




