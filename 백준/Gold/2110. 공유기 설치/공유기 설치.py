N , C = map(int, input().split())
x = list(int(input()) for _ in range(N))
dp  = [0] * N
x.sort()
start = 1
end = x[-1]- x[0]
ans = 0
while start <= end:
    mid = (start+end)//2
    now = x[0]
    cnt = 1
    for i in range(1, N):
        if x[i] >= now + mid:
            cnt += 1
            now = x[i]
    if cnt >= C:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)
