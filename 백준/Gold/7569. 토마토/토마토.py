from collections import deque
import sys
input = sys.stdin.readline
M , N, H = map(int, input().split())

box = []
q = deque()

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
        for m in range(M):
            if row[m]== 1:
                q.append((h, n, m , 0))
    box.append(layer)
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

max_day = 0

while q:
    z, x, y, day = q.popleft()
    max_day = max(max_day, day)
    for k in range(6):
            nz = z + dz[k]
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    q.append((nz, nx, ny, day + 1))


for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)

                sys.exit(0)
print(max_day)
# box = [list(map(int,input().split())) for _ in range(N*H)]
# for i in box:
#     print(i)
#
# def bfs(L ,x, y):
#     q = deque()
#     q.append([x,y])
# dx = [-1, 0, 0, 1]
# dy = [0 , -1, 1 , 0]
# while True:
#     day = 1
#     for h in range(H):
#         for i in range(N*h , N*(h+1)):
#             for j in range(M):
#                 print(h, i , j)
#                 if box[i][j] == 1:
#                     for d in range(4):
#                         nx, ny = i+dx[d] , j+dy[d]
#                         if 0<= nx <= M and N*h <= ny <= N*(h+1) and box[nx][ny] == 0:
#                             box[nx][ny] = 1
#


