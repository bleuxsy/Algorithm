from collections import deque
# def checkbox(grid):
#     for row in grid:
#         for val in row:
#             if val == 0:
#                 return False
#     return True

M , N = map(int, input().split())
stack = deque()
days = [[0] * M for _ in range(N)]
    # 1 : 익은 토마토
    # -1 : 없음
grid = [list(map(int, input().split())) for i in range(N)]


for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            stack.append((i , j))


while stack:
    x , y = stack.popleft()


    dx = [-1 ,0, 0, 1]
    dy = [0 ,-1, 1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M :
            if grid[nx][ny] == 0:
                grid[nx][ny] = 1
                days[nx][ny] = days[x][y] + 1
                stack.append((nx , ny))


max_days = 0
is_impossible = False
for i in range(N):
    for j in range(M):

        if grid[i][j] == 0:
            is_impossible = True
            break

    if is_impossible:
        break

    max_days = max(max_days, max(days[i]))


if is_impossible:
    print(-1)
else:
    print(max_days)