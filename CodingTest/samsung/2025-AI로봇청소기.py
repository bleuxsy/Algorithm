import sys
from collections import deque
import heapq
sys.stdin = open("input.txt", "r")

def bfs(rx, ry, occupied):

    stack = deque()
    visited=[[False] * N for _ in range(N)]
    stack.append((rx, ry, 0))
    visited[rx][ry] = True
    min_dist = -1
    cand = []
    while stack:
        cx, cy, dist = stack.popleft()

        # 이것보다 큰 거는 고려를 안한다 ~
        if min_dist != -1 and  dist > min_dist:
            break
        if grid[cx][cy] > 0 :
            cand.append((cx, cy))
            min_dist = dist
            continue

        for dx , dy in ((-1, 0), (0, -1),  (0, 1), (1, 0)):
            nx , ny = cx + dx , cy + dy

            if  0 <=nx < N and 0<=ny < N and not visited[nx][ny] and grid[nx][ny] != -1 and not occupied[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny , dist+1))

    if cand:
        cand.sort()
        return cand[0]


    return rx, ry
dirs = ((-1, 0), (0, -1),  (0, 1), (1, 0))
def move_robot():
    global robot
    occupied = [[False]*N for _ in range(N)]
    for rx, ry in robot:
        occupied[rx][ry] = True

    new_robot = []
    for rx, ry in robot:
        occupied[rx][ry] = False
        nrx, nry = bfs(rx, ry, occupied)
        new_robot.append((nrx, nry))
        occupied[nrx][nry] = True

    robot = new_robot

    return
def clean():
    for idx in range(len(robot)):
        best = -1
        best_dir = 0
        rx, ry = robot[idx]
        dir_dust = []
        clean_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in range(4):
            t= 0
            if grid[rx][ry] > 0:
                t += min(20, grid[rx][ry])

            for nd in ((d + 3) % 4, d, (d + 1) % 4):
                dx , dy = clean_dirs[nd]
                nx , ny = rx + dx, ry+ dy
                if 0<= nx < N and 0<= ny < N and grid[nx][ny] != -1:
                    t += min(20, grid[nx][ny])

            if t > best:
                best = t
                best_dir = d

        if grid[rx][ry] > 0:
            grid[rx][ry] = max(0, grid[rx][ry]- 20)

        for d in ((best_dir+3)%4 , best_dir, (best_dir+1)%4):
            dx, dy = clean_dirs[d]
            nx, ny = rx+dx , ry + dy

            if 0<= nx < N and 0<= ny < N and grid[nx][ny] > 0:
                grid[nx][ny] = max(0, grid[nx][ny] - 20)
        # for dx , dy in robot_dir[nd]:
        #     nx, ny = rx + dx, ry + dy
        #     if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != -1:
        #         if grid[nx][ny] >= 20:
        #             grid[nx][ny] -= 20
        #         else:
        #             grid[nx][ny] = 0



    return
def add_dust():

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                grid[i][j] += 5


def diffusion():

    grid_n = [g[:] for g in grid]
    for i in range(N):
        for j in range(N):

            if grid[i][j] == 0:
                sumdust = 0
                for dx , dy in dirs:
                    nx , ny = i+ dx, j + dy
                    if 0<= nx < N  and 0<=ny < N:
                        if grid[nx][ny] >0 :
                            sumdust+=grid[nx][ny]
                grid_n[i][j]= sumdust//10


    return grid_n
if __name__ == "__main__":

    N, K , L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    robot = []
    for _ in range(K):
        r, c  = map(int, input().split())
        robot.append((r-1,c-1))

    for _ in range(L) :
        total= 0
        move_robot()
        clean()
        add_dust()
        grid = diffusion()
        for i in range(N):
            for j in range(N):
                if grid[i][j] >= 0:
                    total += grid[i][j]
        print(total)

