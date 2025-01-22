n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for i in range(2)] # dp[1][0] = 0 
dp[0][0] = arr[0]
answer = arr[0]
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[1][i-1] + arr[i], dp[0][i-1])
    answer = max(answer, dp[0][i], dp[1][i])
print(answer)