import heapq

INF = 10**18

def dijkstra(double_u=-1, double_v=-1):
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    pq = []

    dist[1] = 0
    heapq.heappush(pq, (0, 1))

    while pq:
        cur_dist, x = heapq.heappop(pq)

        if dist[x] < cur_dist:
            continue

        for nx, w in graph[x]:
            cost = w

            # 이번에 2배로 늘릴 간선이면 비용 2배
            if (x == double_u and nx == double_v) or (x == double_v and nx == double_u):
                cost = w * 2

            nd = cur_dist + cost
            if dist[nx] > nd:
                dist[nx] = nd
                parent[nx] = x
                heapq.heappush(pq, (nd, nx))

    return dist, parent


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

# 원래 최단거리 + parent 구하기
dist, parent = dijkstra()
original = dist[n]

# path 배열에 원래 최단경로의 간선 저장
path = []
cur = n
while cur != 1:
    prev = parent[cur]
    path.append((prev, cur))
    cur = prev

answer = original

# path 위의 간선만 하나씩 2배로 바꿔서 다시 다익스트라
for u, v in path:
    new_dist, _ = dijkstra(u, v)
    answer = max(answer, new_dist[n])

print(answer - original)