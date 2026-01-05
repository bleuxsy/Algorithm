
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])



# def back(total, start):
#     global cnt
#     if total == N:
#         cnt += 1
#         return
#     for x in (1, 2, 3):
#         if x < start:
#             continue
#         if total + x <= N:
#             back(total + x, x)
#
# T = int(input())
# for j in range(T):
#     N = int(input())
#     cnt = 0
#     back(0,1)
#     print(cnt)
