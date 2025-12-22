N = int(input())
money = list(map(int, input().split()))
M = int(input())
minM = M // len(money)

left = 0
right = max(money)
res = 0

while left <= right:
    mid = (left+right) // 2
    total = 0

    for m in money:
        total += min(m, mid)
    if total <= M:
        answer = mid
        left = mid+1
    else:
        right = mid -1

print(answer)