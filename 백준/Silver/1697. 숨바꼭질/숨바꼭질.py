#1697
import sys
from collections import deque
def bfs(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if v == K:
      return visit[v]
    for i in (v-1,v+1,2*v):
      if 0<= i < MAX and not visit[i]:
        visit[i] = visit[v]+1
        q.append(i)
MAX = 100001
N, K = map(int,input().split())
visit = [0]*MAX
print(bfs(N))