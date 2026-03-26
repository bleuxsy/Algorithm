import heapq

n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

INF = 10 ** 18
dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def find(x, y):
    D = [[INF] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    pq = []

    D[x][y] = 0
    heapq.heappush(pq, (0, x, y))

    while pq:
        dist, sx, sy = heapq.heappop(pq)

        if visited[sx][sy]:
            continue

        visited[sx][sy] = True

        for dx, dy in dirs:
            nx = sx + dx
            ny = sy + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == grid[sx][sy]:
                    cost = a
                else:
                    cost = b

                if D[nx][ny] > dist + cost:
                    D[nx][ny] = dist + cost
                    heapq.heappush(pq, (D[nx][ny], nx, ny))

    max_val = 0
    for i in range(n):
        for j in range(n):
            if D[i][j] != INF:
                max_val = max(max_val, D[i][j])

    return max_val

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, find(i, j))

print(answer)