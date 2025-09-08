import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(N)]
xy = [list(map(int, input().split())) for _ in range(M)]

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = mylist[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]


for j in range(M):
    x1, y1, x2, y2 = xy[j]


    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)