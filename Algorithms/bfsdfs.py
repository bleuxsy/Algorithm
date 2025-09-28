import sys
from collections import deque
sys.stdin = open("inx.txt", "r")
def bfs(s):
    q = []
    q.append(s)

    ans.append(s)
    visited[s] = 1
    while q:
        c = q.pop(0)
        for n in lst[c]:
            if not visited[n]:
                q.append(n)
                ans.append(n)
                visited[n] = 1



def dfs( v):
    ans.append(v)
    visited[v] = 1
    for n in lst[v]:
        if not visited[n]:
            dfs(n)



if __name__ == "__main__":
    N , M , V = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    for _ in range(M):
        si, sj = map(int, input().split())
        lst[si].append(sj)
        lst[sj].append(si)
        lst[si].sort()
        lst[sj].sort()

    visited = [0]* (N + 1)
    ans = []
    print(visited)
    print(lst)
    dfs(V)
    print(ans)
    visited = [0] * (N + 1)
    ans = []
    bfs(V)
    print(ans)