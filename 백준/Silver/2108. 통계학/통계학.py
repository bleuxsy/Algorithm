import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

a= int(round(sum(num)/N, 0))

num.sort()

mid = N//2
b = num[mid]
cnt = {}
for k in num:
    if k not in cnt:
        cnt[k] = 0
    cnt[k] += 1
res = sorted(cnt, key = lambda x : cnt[x], reverse=True)
if len(res) == 1:
    c = res[0]
elif cnt[res[0]] == cnt[res[1]]:
    c = res[1]
else:
    c = res[0]
d = max(num) - min(num)


print(a)
print(b)
print(c)
print(d)
