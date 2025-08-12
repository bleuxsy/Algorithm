from collections import deque
def solution(n, edge):
    answer = 0
    count = [0] * (n+1)
    visited = [False] * (n+1)
    graph = deque()
    vert = {}
    for a, b in edge:
        if a not in vert:
            vert[a] = []
        vert[a].append(b)
        if b not in vert:
            vert[b] = []
        vert[b].append(a)
    
    graph.append(1)
    visited[1] = True
    count[1] = 1
    while graph:
        now = graph.popleft()
        for nxt in vert[now]:
            if not visited[nxt]:
                visited[nxt] = True
                count[nxt] = count[now] + 1
                graph.append(nxt)
        # if not visited[now] :
        #     graph.extend(vert[now])
        #     for i in vert[now]:
        #         if count[i] == 0:
        #             count[i] = count[now] + 1
        #     visited[now] = True
            
    max_num = max(count)
    answer = sum(1 for c in count if c == max_num)
    return answer