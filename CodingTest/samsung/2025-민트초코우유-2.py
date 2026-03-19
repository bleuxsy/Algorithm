import sys
from collections import deque
sys.stdin = open("input.txt", "r")
def printResult():
    # 민:1 초:2 우:4 초우:5 민초:3 민초우:7

    print("신봉하는 음식")
    for f in F:
        print(*f)

    print("신앙심")
    for b in B:
        print(*b)

def morning():
    global F, B
    print("===========아침=============")
    for i in range(N):
        for j in range(N):
            B[i][j] += 1


def bfs(x, y):
    global visited
    stack = deque([(F[x][y], x, y)])
    group = [(B[x][y], x, y, F[x][y])]
    while stack:
        sf, sx, sy = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and F[nx][ny] == sf:
                    stack.append((F[nx][ny] , nx, ny))
                    group.append((B[nx][ny], nx, ny, F[nx][ny]))
                    visited[nx][ny] = 1
    return group


def lunch():
    # 점심
    print("===========점심=============")

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                groups = bfs(i, j)
                groups = sorted(groups, key = lambda x: (-x[0], x[1], x[2]))
                print(*groups)
                for k in range(len(groups)):

                    if k == 0 :
                        print("대표자")
                        print(*groups[k])
                        master.append(groups[k])

                        B[groups[k][1]][groups[k][2]] += (len(groups)-1)
                    else:
                        B[groups[k][1]][groups[k][2]] -=1

    return
def evening():
    group_ord = {1:1 , 2:1, 4:1, 6:2, 5:2, 3:2, 7:3}
    order = []
    for m in range(len(master)):
        order.append([group_ord[master[m][3]], -master[m][0] , master[m][1], master[m][2]])

    order = sorted(master, key=lambda x: (group_ord[x[3]], -x[0], x[1], x[2]))
    blocked = [[False] * N for _ in range(N)]

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위 아래 왼 오

    for faith, sx, sy, food in order:

        if blocked[sx][sy]:
            continue

        d = B[sx][sy] % 4
        x = B[sx][sy] - 1
        B[sx][sy] = 1

        step = 1
        while x > 0:
            nx = sx + dirs[d][0] * step
            ny = sy + dirs[d][1] * step

            if not (0 <= nx < N and 0 <= ny < N):
                break

            if F[nx][ny] == F[sx][sy]:
                step += 1
                continue

            y = B[nx][ny]


            if x > y:
                x -= (y + 1)
                F[nx][ny] = F[sx][sy]
                B[nx][ny] += 1
                blocked[nx][ny] = True


            else:
                F[nx][ny] |= F[sx][sy]
                B[nx][ny] += x
                blocked[nx][ny] = True
                x = 0

            step += 1
def calculate():
    result = [0] * 8
    for i in range(N):
        for j in range(N):
            result[F[i][j]] += B[i][j]

    print(result[7], result[3], result[5], result[6], result[4], result[2], result[1])



    return
if __name__ == "__main__":

    N, T = map(int, input().split())

    F = list(list(input()) for _ in range(N))
    B = [list(map(int, input().split())) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if F[j][i] == 'T':
                F[j][i] = 1
            elif F[j][i] == "C":
                F[j][i] = 2
            else:
                F[j][i] = 4


    for _ in range(T):
        printResult()
        morning()
        printResult()
        visited = [[0 for _ in range(N)] for _ in range(N)]
        master = []
        lunch()
        printResult()
        evening()
        printResult()
        result = [0] * 8
        calculate()


