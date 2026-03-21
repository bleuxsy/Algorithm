import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
a, b = map(int, input().split())

path = []

pq = []
graph = [[]* (n+1) for _ in range(n+1)]

for a, b, d in edges:
    graph[a].append((b, d))


print(graph)