from collections import deque

# 이동: 상,우,하,좌 (BFS에서 거리 최소 + 행/열 최소를 위해)
mv = [(-1,0),(0,1),(1,0),(0,-1)]

# 청소 방향 우선순위: 오른쪽, 아래, 왼쪽, 위
dir4 = [(0,1),(1,0),(0,-1),(-1,0)]

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move():

    new_robot_list = []

    occupied = [[False]*N for _ in range(N)]
    for x,y in robot_list:
        occupied[x][y] = True

    for sx,sy in robot_list:

        occupied[sx][sy] = False

        q = deque([(sx,sy,0)])
        visited = [[0]*N for _ in range(N)]
        visited[sx][sy] = 1

        min_dist = -1
        cand = []

        while q:

            x,y,dist = q.popleft()

            if min_dist != -1 and dist > min_dist:
                break

            if grid[x][y] > 0:
                cand.append((x,y))
                min_dist = dist
                continue

            for d in range(4):

                nx = x + dx[d]
                ny = y + dy[d]

                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:

                    if grid[nx][ny] != -1 and not occupied[nx][ny]:

                        visited[nx][ny] = 1
                        q.append((nx,ny,dist+1))

        if cand:
            cand.sort()
            tx,ty = cand[0]
        else:
            tx,ty = sx,sy

        new_robot_list.append((tx,ty))
        occupied[tx][ty] = True

    return new_robot_list


def clean():

    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    for i,j in robot_list:

        best = -1
        best_dir = 0

        for d in range(4):

            total = min(20,grid[i][j])

            for nd in [(d+3)%4,d,(d+1)%4]:

                nx = i + dir[nd][0]
                ny = j + dir[nd][1]

                if 0<=nx<N and 0<=ny<N and grid[nx][ny] > 0:
                    total += min(20,grid[nx][ny])

            if total > best:
                best = total
                best_dir = d

        if grid[i][j] > 0:
            grid[i][j] = max(0,grid[i][j]-20)

        for nd in [(best_dir+3)%4,best_dir,(best_dir+1)%4]:

            nx = i + dir[nd][0]
            ny = j + dir[nd][1]

            if 0<=nx<N and 0<=ny<N and grid[nx][ny] > 0:
                grid[nx][ny] = max(0,grid[nx][ny]-20)



def diffusion():

    new_grid = [row[:] for row in grid]

    for i in range(N):
        for j in range(N):

            if grid[i][j] == 0:

                total = 0

                for d in range(4):

                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0<=nx<N and 0<=ny<N and grid[nx][ny] > 0:
                        total += grid[nx][ny]

                new_grid[i][j] = total//10

    return new_grid


def printResult():
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                ans += grid[i][j]
    print(ans)


# ---------- input ----------
N,K,L = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

robot_list = []

for _ in range(K):
    r,c = map(int,input().split())
    robot_list.append((r-1,c-1))

for _ in range(L):

    robot_list = move()

    clean()

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                grid[i][j] += 5

    grid = diffusion()

    ans = 0
    for r in grid:
        for v in r:
            if v > 0:
                ans += v

    print(ans)