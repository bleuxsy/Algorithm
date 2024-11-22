N = int(input())
A = list(map(int,input().split()))
dp= [1] * N
for i in range(N):
  for j in range(i):
    if A[i] > A[j]:
      dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
arr = []
order = max(dp)
for i in range(N-1, -1, -1):
  if dp[i] == order:
    arr.append(A[i])
    order -= 1
arr.reverse()
print(*arr)