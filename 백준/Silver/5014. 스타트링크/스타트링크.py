from collections import deque

F, S, G, U, D = map(int, input().split())

dp = [-1] * (F + 1)
q = deque()

q.append(S)
dp[S] = 0

while q:
    now = q.popleft()
    if now == G:
        break

    for move in (U, -D):
        nxt = now + move
        if 1 <= nxt <= F and dp[nxt] == -1:
            dp[nxt] = dp[now] + 1
            q.append(nxt)

if dp[G] == -1:
    print("use the stairs")
else:
    print(dp[G])