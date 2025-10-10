from collections import deque

def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    min_diff = n  # 초기값 크게
    for a, b in wires:
        visited = [0] * (n+1)
        visited[a] = 1
        visited[b] = -1
        
        q = deque([a])
        while q:
            cur = q.popleft()
            for nxt in tree[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    q.append(nxt)
        
        cnt = visited.count(1)
        diff = abs(n - 2*cnt)
        min_diff = min(min_diff, diff)
    
    return min_diff