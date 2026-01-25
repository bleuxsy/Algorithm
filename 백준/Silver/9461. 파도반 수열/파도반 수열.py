T = int(input())
arr = [int(input()) for _ in range(T)]

max_n = max(arr)
dp = [0] * (max_n + 1)

dp[1] = dp[2] = dp[3] = 1
for i in range(4, max_n + 1):
    dp[i] = dp[i-3] + dp[i-2]

for n in arr:
    print(dp[n])