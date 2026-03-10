def back(L, t):
    global answer
    if L == n:
        answer = max(answer, t)
        return
    c = 0
    r = 0
    for i in range(n):
        if not col[i]:
            c = i
    for i in range(n):
        if not raw[i]:
            r = i

    col[c] = 1
    raw[r] = 1


    back(L + 1, t + grid[c][r])

    col[c] = 0
    raw[r] = 0




n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
col = [0] * n
raw = [0] * n
answer = 0
back(0, 0)
# Please write your code here.
print(answer)