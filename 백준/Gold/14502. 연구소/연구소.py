from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(walls):
    grid = [row[:] for row in real_grid]  # deepcopy 대신 얕은 복사
    
    # 벽 세우기
    for x, y in walls:
        grid[x][y] = 1

    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                q.append((nx, ny))

    return sum(row.count(0) for row in grid)

N, M = map(int, input().split())
real_grid = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸과 바이러스 좌표 미리 수집
empty = [(i, j) for i in range(N) for j in range(M) if real_grid[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if real_grid[i][j] == 2]

answer = 0
for walls in combinations(empty, 3):  # 빈 칸 중 3곳만 선택
    answer = max(answer, bfs(walls))

print(answer)