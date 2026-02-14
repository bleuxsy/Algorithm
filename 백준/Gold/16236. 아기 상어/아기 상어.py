from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

shark = 2
eat = 0
res = 0

# 시작 위치 찾기
sx = sy = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            sx, sy = i, j
            grid[i][j] = 0

def bfs(sx, sy, shark):
    q = deque()
    q.append((sx, sy))

    visited = [[False]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    visited[sx][sy] = True

    can_eat = []

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

                if grid[nx][ny] <= shark:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


                    if 0 < grid[nx][ny] < shark:
                        can_eat.append((dist[nx][ny], nx, ny))

    can_eat.sort()
    return can_eat

while True:
    fishlist = bfs(sx, sy, shark)

    if not fishlist:
        print(res)
        break

    mvt, nx, ny = fishlist[0]  
    res += mvt
    sx, sy = nx, ny

    # 먹기
    grid[sx][sy] = 0
    eat += 1

    if eat == shark:
        shark += 1
        eat = 0