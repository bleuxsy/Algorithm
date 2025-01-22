from collections import deque

N, K = map(int, input().split())
visited = [0] *100001
check = [0] *100001

def move(now):
    data = []
    temp = now
    for j in range(visited[now]+1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    q = deque()
    q.append(N)

    while q:
        now = q.popleft()
        if now == K:
            print(visited[now])
            move(now)
            return now
        for i in (now+1, now-1 , now*2):
            if 0<=i<=100000 and visited[i]==0:
                q.append(i)
                visited[i] = visited[now]+1
                check[i]= now
bfs()        