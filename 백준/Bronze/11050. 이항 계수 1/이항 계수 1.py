N, K = map(int,input().split())
result = 1
for i in range(K):
  result *= N
  N -=1
M = 1
for i in range(2, K+1):
  M *= i
print(result//M)