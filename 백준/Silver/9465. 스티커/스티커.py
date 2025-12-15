import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*N for _ in range(2)]

    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]

    if N >= 2:
        dp[0][1] = dp[1][0] + grid[0][1]
        dp[1][1] = dp[0][0] + grid[1][1]

    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + grid[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + grid[1][i]

    print(max(dp[0][N-1], dp[1][N-1]))
# def dfs(x, y, total):
#     visited[x][y] = 1
#
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < 2 :
#             visited[nx][ny] = 1
#             dfs()
