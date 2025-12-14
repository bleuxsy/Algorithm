N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M+1)]* (N+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + grid[i-1][j-1]
print(dp[N][M])



# dfs
# dx = [1, 0, 1]   # 아래, 오른쪽, 대각선
# dy = [0, 1, 1]
#
# res = 0
# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
#
# def dfs(L, x, y):
#     global res
#     if x == N-1 and y == M-1:
#         res = max(res, L)
#         return
#
#     for d in range(3):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
#             visited[nx][ny] = True
#             dfs(L + grid[nx][ny], nx, ny)
#             visited[nx][ny] = False
#
# visited[0][0] = True
# dfs(grid[0][0], 0, 0)
# print(res)