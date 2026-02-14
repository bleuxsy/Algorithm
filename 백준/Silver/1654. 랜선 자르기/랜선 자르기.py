import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

lo, hi = 1, max(lans)   # 길이는 1부터 가능 (0은 불가)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for l in lans:
        cnt += l // mid

    if cnt >= N:        # mid 길이로 N개 이상 만들 수 있으면 길이를 늘려봄
        ans = mid
        lo = mid + 1
    else:               # N개 못 만들면 길이를 줄임
        hi = mid - 1

print(ans)






# 시간 초과 --> 이분 탐색 활용
# K , N = map(int, input().split())
# lans = list( int(input()) for _ in range(K))
#
# L = max(*lans)
# maxres = 0
# for cm in range(2, L):
#     cnt  = 0
#     for l in lans:
#         cnt += l//cm
#     if cnt >= N:
#         maxres= max(maxres , cm)
# print(maxres)