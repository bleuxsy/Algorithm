from collections import deque
res = 0

N = int(input())
r1, c1, r2, c2 = map(int,input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
stack = deque()
stack.append((r1,c1))
visited = list([-1] * N for _ in range(N))
visited[r1][c1] = 0
while stack:
    sx, sy = stack.popleft()
    if sx == r2 and sy == c2:
        break
    for d in range(6):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if 0<= nx < N and 0 <= ny < N :
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[sx][sy] +1
                stack.append((nx,ny))
print(visited[r2][c2])
