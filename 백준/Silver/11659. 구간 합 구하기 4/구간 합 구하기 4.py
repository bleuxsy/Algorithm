import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = list(map(int, input().split()))

pre = [0] * (N + 1)
for i in range(N):
    pre[i + 1] = pre[i] + n[i]

out = []
for _ in range(M):
    i, j = map(int, input().split())
    out.append(str(pre[j] - pre[i - 1]))

sys.stdout.write("\n".join(out))