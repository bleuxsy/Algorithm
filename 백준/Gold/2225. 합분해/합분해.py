MON = 1000000000
def count_ways(N,K):
  dp = [[0] * (N+1) for _ in range(K+1)]
  dp[0][0] = 1
  for k in range(1,K+1):
    for s in range(N+1):
      for x in range(N+1):
        if s - x >= 0:
          dp[k][s] = (dp[k][s] + dp[k-1][s-x]) % MON
  return dp[K][N]


N, K = map(int,input().split())
print(count_ways(N,K))
