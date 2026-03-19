from collections import deque


def bfs(x, y):
    stack = deque()
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    stack.append((x, y, 0))
    while stack:
        sx, sy, t = stack.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if grid[nx][ny] == 2:
                        box[x][y] = t + 1
                        return

                    elif grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny, t + 1))
            print(stack)
    return


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
box = [[-2] * n for _ in range(n)]
# Please write your code here.
# 귤 . bfs로 풀어야 함.


for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            box[i][j] = -1
        elif grid[i][j] == 1:

            bfs(i, j)
        else:
            box[i][j] = 0
for b in box:
    print(*b)
