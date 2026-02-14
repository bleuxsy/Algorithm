import heapq

MAX = 1e9
def dijkstra(start):
    time = [MAX]*(N+1)
    time[start]= 0
    q = []
    heapq.heappush(q, (0 , start))
    while q:
        dist, now = heapq.heappop(q)
        if time[now] >= dist:
            for v, val in road[now]:
                if dist+val < time[v]:
                    time[v] = dist+ val
                    heapq.heappush(q, (dist+val , v))
    return time
N , M , X = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    road[s].append([e, t])
ans = dijkstra(X)
ans[0] =0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]

print(max(ans))
