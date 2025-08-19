N = int(input())

TP = [list(map(int, input().split())) for i in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i + TP[i][0] , N+1):
        if dp[j] < dp[i] + TP[i][1]:
            dp[j] = dp[i] + TP[i][1]
print(dp[-1])