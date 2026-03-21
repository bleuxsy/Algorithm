"""
djikstra
그래프 : 인접리스트
graph[(숫자)] = [(변환된 숫자, 비용) , (변환된 숫자, 비용)()]

점프:
    상하좌우
점프력 증가 :

    점프력의 제곱만큼 비용
점프력 감소:
    점프력 비용 1
노드 번호 = (행, 열, 점프력) -> 변환된 숫자
"""
import heapq
from collections import deque
N = int(input())
grid = [
    list(input()) for _ in range(N)
]
# 그래프 만들기
graph = [[] for _ in range(50*50*5+5)]
drs, dcs = [[1, -1, 0, 0], [0, 0, 1, -1]]


def in_range(r, c):
    return 0<= r< N and 0<= c < N
def state_to_number(r, c, jump):

    return (jump-1) + c * 5 + r*5 *50
def number_to_state(number):
    r = number // (5*50)
    number %= 50*50
    c = number //5
    number %= 5
    jump = number +1
    return (r, c, jump)

for r in range(N):
    for c in range(N):
        if grid[r][c] != '.':
            continue
        for jump in range(1, 6):
            """
                점프력 증가
            """
            if jump <= 4:
                curr = state_to_number(r, c, jump)
                nxt = state_to_number(r, c, jump+1)
                graph[curr].append((nxt, (jump+1)**2))

            """
                점프력 감소
            """
            if jump > 1:
                curr = state_to_number(r, c, jump)
                for next_jump in range(1, jump):
                    nxt = state_to_number(r,c, next_jump)
                    graph[curr].append((nxt, 1))
            """
                점프
            """

            for dr, dc in zip(drs, dcs):
                nr, nc = r, c
                is_valid = True
                # 천적이 있거나 미끄러운 돌이면 False
                for _ in range(jump):
                    nr, nc = nr + dr , nc + dc
                    if not in_range(nr, nc) or grid[nr][nc] == '#':
                        is_valid = False
                        break
                if is_valid and grid[nr][nc] == ".":
                    #도착 지점이 미끄러운 돌인지
                    nxt = state_to_number(nr, nc, jump)
                    curr = state_to_number(r, c, jump)
                    graph[curr].append((nxt, 1))





Q = int(input())
for _ in range(Q):
    sr, sc, er, ec = map(int, input().split())
    sr, sc, er, ec = sr-1, sc-1, er-1, ec-1
    #다익스트라
    visited = [False]*(5*50*50 + 5)
    curr = state_to_number(sr, sc, 1)
    D = [float('inf')] * (5*50*50+5)

    pq = []
    heapq.heappush(pq, (0, curr))



    while pq:
        dist, curr = heapq.heappop(pq )
        if visited[curr]:
            continue

        visited[curr] = True

        for nxt, w in graph[curr]:
            if D[nxt] > dist+w and not visited[nxt]:
                D[nxt] = dist+w
                heapq.heappush(pq, (D[nxt], nxt))
    ans = float('inf')
    for jump in range(1, 6):
        state = state_to_number(er, ec, jump)
        ans = min(ans, D[state])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


