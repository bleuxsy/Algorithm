from collections import deque

T = int(input())
for _ in range(T):
    stack = deque()
    bug = 0
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        grid[b][a] = 1  # (x=a, y=b)

    for y in range(N):  # 행
        for x in range(M):  # 열
            if grid[y][x] == 1 and not visited[y][x]:
                stack.append((x, y))
                visited[y][x] = True
                while stack:
                    sx, sy = stack.popleft()
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nx, ny = sx + dx, sy + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if grid[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                stack.append((nx, ny))
                bug += 1
    print(bug)