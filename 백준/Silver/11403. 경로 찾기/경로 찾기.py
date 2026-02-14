from collections import deque


N =  int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N  for _ in range(N)]


def bfs(x):
    q = deque()
    q.append(x)
    flag = [0 for _ in range(N)]

    while q:
        n = q.popleft()

        for i in range(N):
            if flag[i] == 0 and grid[n][i] == 1:
                q.append(i)
                flag[i] = 1
                visited[x][i] = 1
for i in range(N):
    bfs(i)

for v in visited:
    print(*v)
    #리스트의 각 요소를 공백으로 구분해 출력

# for i in range(N):
#     for j in range(N):
#         if grid[i][j] == 1:
#             stack[i].append(j)
#
# print(stack)
#
# for i in range(N):
#
#     for j in range(len(stack[i])):
#         n = stack[i][j]
#         d.append(n)
#         new_grid[i][n] = 1


