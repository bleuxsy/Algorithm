from collections import deque
N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
count = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (N+1)
distance[0] = 0
d = deque(X)
now = d.popleft()
for next in graph[now]:
    if distance[next] == -1:
        distance[next] = distance[now]+1       
        d.append(next)
flag = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        flag = True
if flag == False:
    print(-1)
