N , D = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
dp = [1e9] * (D+1)
dp[0]= 0
for i in range(1, D+1):
    dp[i] = dp[i-1] + 1
    for s, e, l in road:
        if i == e:
            dp[i] = min(dp[i], dp[s]+ l)
            
print(dp[D])

