#1676
N = int(input())
Alist = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
  for j in range(i):
    if Alist[i]< Alist[j]:
      dp[i] = max(dp[i],dp[j]+1)
print(max(dp))