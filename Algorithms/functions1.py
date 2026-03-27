import heapq
INF = 10**18
n, m, X = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visited = [False] * (n+1)

grid = [[] for _ in range(n+1)]
back_grid = [[] for _ in range(n+1)]
for x,y,w in edges:
    grid[x].append((y,w))

for x,y, w in edges:
    back_grid[y].append((x,w))

print(grid)
print(back_grid)

# [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], [(2, 3)]]
pq = []
D = [INF] * (n+1)
"""
    D : X 정점에서 다른 정점까지의 최단 거리  ( X -> ??)
    B : 다른 정점에서 X까지의 최단 거리 (X에서 다른 정점까지의 거리) ( ?? -> X)
    

"""
heapq.heappush(pq, (0, X))
D[X] = 0




while pq :
    w , sx = heapq.heappop(pq)

    if visited[sx]:
        continue
    visited[sx] = True

    for nx , nw in grid[sx]:
        if D[nx] > D[sx] + nw:
            D[nx] = D[sx] + nw
            heapq.heappush(pq, (D[nx], nx))

pp = []
print(D)
visited = [False] * (n+1)
B = [INF] * (n+1)
heapq.heappush(pp, (0, X))

B[X] = 0

while pp:
    w, sx = heapq.heappop(pp)

    if visited[sx]:
        continue
    visited[sx] = True

    for nx, nw in back_grid[sx]:
        if B[nx] > B[sx] + nw:
            B[nx] = B[sx] + nw
            heapq.heappush(pp, (B[nx], nx))

answer = 0
print(B)
for i in range(1, n+1):
    if answer < D[i] + B[i]:
        answer = D[i] + B[i]

print(answer)