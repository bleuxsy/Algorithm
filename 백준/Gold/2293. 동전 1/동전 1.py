n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
coin.sort()
dp = [0] * (k+1)
dp[0] = 1
for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])