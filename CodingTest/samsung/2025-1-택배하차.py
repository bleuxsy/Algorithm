import sys
from collections import deque
import heapq
sys.stdin = open("input.txt", "r")

def result_print(txt=None, lst = None):
    if txt is not None:

        print(txt)

    for g in lst:
        print(*g)
def check(idx, lr):
    dirs = ((0, -1), (0, 1))
    x, y, h, w = box[idx]

    for  i in range(x, x+h):
        cx , cy = i, y
        while True:
            dx , dy =dirs[lr]
            nx, ny = cx+ dx , cy + dy
            if 0<= nx < N and 0<= ny < N :

                if grid[nx][ny] == idx or grid[nx][ny] == 0:
                    cx , cy = nx, ny
                    continue
                else:

                    return False
            break

    return True

def add_box(k, sx, sy, h, w ):
    global box
    global grid

    min_bx = N-1

    for i in range(sy , sy+w):
        for j in range(sx + h-1, N):
            cx , cy = j, i
            nx , ny = cx + 1 , cy

            if 0<= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                continue

            else:
                min_bx = min(min_bx, cx)


    # 상자 채우기
    for i in range(min_bx, min_bx-h , -1):
        for j in range(sy, sy+w):
            grid[i][j] = k
    box[k] = (min_bx-h+1, sy, h, w)

    return
def left_move():
    global answer
    global grid
    for_move = set()

    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                for_move.add(grid[i][j])
                break


    for_move = list(for_move)
    for_move.sort()

    while for_move:
        for_left = for_move.pop(0)

        if check(for_left, 0):
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == for_left:
                        grid[i][j] = 0
            answer.append(for_left)

            blocked[for_left] = True
            break

    return
def weight(grid):
    new_grid = [[0] * N for _ in range(N)]
    global box


    for idx in b :

        if not blocked[idx]:
            x, y, h, w = box[idx]
            min_bx = N - 1
            for i in range(y, y+w):
                for j in range(x+h-1, N ):
                    cx, cy = j , i
                    nx , ny = cx + 1, cy

                    if 0<= nx < N and 0<= ny < N and new_grid[nx][ny] == 0:
                        continue
                    else:
                        min_bx = min(min_bx, cx)

            for i in range(min_bx, min_bx - h, -1):
                for j in range(y, y + w):
                    new_grid[i][j] = idx

            box[idx] = (min_bx - h + 1, y, h, w)

    return new_grid

def right_move():
    global answer
    global grid
    for_move = set()

    for i in range(N):
        for j in range(N-1, -1, -1):
            if grid[i][j] != 0:
                for_move.add(grid[i][j])
                break

    for_move = list(for_move)
    for_move.sort()

    while for_move:
        for_right = for_move.pop(0)
        if check(for_right, 1):
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == for_right:
                        grid[i][j] = 0
            answer.append(for_right)
            blocked[for_right] = True
            break

    return

if __name__ == "__main__":
    answer = []
    N , M = map(int, input().split())
    b = []
    box = {}

    for _ in range(M):
        k, h, w, c = map(int, input().split())
        box[k] = [0 , c-1, h, w]
        b.append(k)

    B = sorted(b)
    max_B = max(B)

    blocked = [True] * (max_B+1)

    grid = [[0]* N for _ in range(N)]


    for k in b:
        x, y, h, w = box[k]
        blocked[k] = False
        add_box(k, x, y, h, w)


    while True:


        left_move()

        flag = False
        for blk in blocked:
            if not blk :
                flag = True
        if not flag:

            break

        grid = weight(grid)

        right_move()

        flag = False
        for blk in blocked:
            if not blk :
                flag = True
        if not flag:

            break
        grid = weight(grid)

    for a in answer:
        print(a)
