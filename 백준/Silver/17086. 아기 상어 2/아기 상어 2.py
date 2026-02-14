from collections import deque
N , M = map(int, input().split())
dx = [ 1, 1, 0, -1, -1, 0, -1, 1]
dy = [ 1, 0, 1, 1 , 0, -1, -1,-1]
grid = list(list(map(int,input().split())) for _ in range(N))

stack = deque()
res = 0
def bfs():
    while stack:
        sx, sy = stack.popleft()

        for d in range(8):
            nx = sx + dx[d]
            ny = sy + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = grid[sx][sy] +1
                    stack.append([nx,ny])

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            stack.append([i, j])

bfs()
for g in grid:
    res = max(max(g), res)
print(res -1)




