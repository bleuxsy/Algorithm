"""


    사다리가 나오면 위로 올라가고 뱀이 나오면 아래로 내려감.
    1번칸에서 시작해서 100번 칸에 도착
    100번 칸에 도착하기 위해 주사위를 굴려야하는 횟수의 최솟값을 구하시오

    주사위는 1부터 6까지의 숫자

    항상 100번 칸에 도착할 수 있는 입력만 주어짐

    dfs 최단 거리
"""
from collections import deque
def bfs():
    q = deque()

    q.append((1, 0))
    visited[1] = True

    while q:
        x , cnt = q.popleft()

        if x == 100:
            return cnt
        for dice in range(1, 7):
            nx = x+dice
            if nx > 100:
                continue
            if nx in move:
                nx = move[nx]

            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt+1))





N , M = map(int, input().split())
answer = 10 **18
ladder = []
visited = [False] * 101
move = dict()

for _ in range(N):
    u, v = map(int, input().split())
    move[u] = v

for _ in range(M):
    u, v = map(int, input().split())
    move[u] = v

print(bfs())