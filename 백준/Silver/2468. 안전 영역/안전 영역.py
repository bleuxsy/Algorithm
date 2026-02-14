from collections import deque
stack = deque()
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
MAX_HEIGHT = max(max(row) for row in lst)
answer = 1
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for h in range(1, MAX_HEIGHT):
    res = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if h < lst[i][j] and not visited[i][j]:
                res += 1
                stack = deque([(i, j)])
                visited[i][j] = True

            while stack:
                sx, sy = stack.popleft()
                for d in range(4):
                    nx , ny = sx + dx[d], sy + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if lst[nx][ny] > h and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    answer = max(answer, res)
print(answer)