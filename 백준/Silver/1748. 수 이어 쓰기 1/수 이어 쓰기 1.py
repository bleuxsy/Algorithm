N = int(input())
K = len(str(N))  
dp = [0] * (K + 1) 

for i in range(1, K + 1): 
    dp[i] = 9 * i * 10**(i - 1)

total = 0
for i in range(1, K):  
    total += dp[i]


total += (N - 10**(K-1) + 1) * K

print(total)
