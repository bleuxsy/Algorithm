import copy
from collections import deque
N = int(input())
# grid = [list(map(int, input())) for _ in range(N)]
grid = [list(input()) for _ in range(N)]
grid_2 = copy.deepcopy(grid)

visited = list([False] * N for _ in range(N))

for i in range(N):
    for j in range(N):
        if grid_2[i][j] == "G":
            grid_2[i][j] = "R"


stack = deque()
person = 0
nonperson = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            stack.append((i,j))
            while stack:
                sx, sy = stack.popleft()
                for dx , dy in ((1,0), (-1, 0), (0, 1), (0, -1)):
                    nx , ny = sx + dx, sy + dy
                    if 0<= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        
                        if grid[nx][ny] == grid[sx][sy]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
            person += 1
visited = list([False] * N for _ in range(N))
stack = deque()
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            stack.append((i,j))
            while stack:
                sx, sy = stack.popleft()
                for dx , dy in ((1,0), (-1, 0), (0, 1), (0, -1)):
                    nx , ny = sx + dx, sy + dy
                    if 0<= nx < N and 0 <= ny < N and not visited[nx][ny]:

                        if grid_2[nx][ny] == grid_2[sx][sy]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
            nonperson += 1

print(person)
print(nonperson)