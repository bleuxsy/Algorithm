from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001
time = [0] * 100001

def bfs(start, target):
    q = deque()
    q.append(start)
    visited[start] = True 
    
    while q:
        now = q.popleft()
        
        if now == target:  
            return time[now]

       
        if 0 <= now * 2 < 100001 and not visited[now * 2]:
            q.appendleft(now * 2) 
            time[now * 2] = time[now] 
            visited[now * 2] = True

     
        if 0 <= now - 1 < 100001 and not visited[now - 1]:
            q.append(now - 1)  
            time[now - 1] = time[now] + 1
            visited[now - 1] = True

       
        if 0 <= now + 1 < 100001 and not visited[now + 1]:
            q.append(now + 1) 
            time[now + 1] = time[now] + 1
            visited[now + 1] = True

print(bfs(N, K))
