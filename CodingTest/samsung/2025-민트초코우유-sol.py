import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(v, si, sj):
    q = deque()
    food = farr[si][sj]
    blst = []
    q.append((si, sj))
    v[si][sj] = food
    blst.append([- barr[si][sj], si , sj])
    while q:
        ci, cj = q.popleft()

        # 네방향, 범위내, 미방문, 조건
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di , cj+dj
            if 0<= ni < N and 0 <= nj < N and v[ni][nj] == 0 and farr[ni][nj] == food:
                q.append((ni, nj))
                v[ni][nj] = food
                blst.append([ -barr[ni][nj], ni, nj])

    # 대표자 리턴
    blst.sort()
    _ , bi, bj = blst[0]
    barr[bi][bj] += len(blst)       #대표자는 그룹 인원수 만큼 신앙심 +

    return bi, bj




# [1]대표자 리스트(전파할 우선순위) [ 우선순위, - 신앙심, 행 , 열]
# 단일 : 민트 , 초코 , 우유 , 이중 : 초코우유 , 민트우유, 민트초코, 삼중: 민초우
group_ord = {4:1, 2:1, 1:1, 3:2, 5:2, 6:2, 7:3}
def group():
    boss = []
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                # 대표자 리턴
                ti, tj= bfs(v, i , j)
                food = farr[ti][tj]         #대표자 음식 => 우선순위
                boss.append([group_ord[food], -barr[ti][tj], ti, tj]) #전파하는 우선순위
    return boss

dirs = [(-1,0), (1,0), (0,-1), (0, 1)]
def move(blst):
    moved = set() # 전파 당했냐? 확인용
    for _, cn, ci, cj in blst:
        if (ci, cj) in moved : #당일에 이미 전파 당한 경우 전파하지 않음
            continue
        cn = -cn
        di, dj = dirs[cn%4] # 전파 방향
        score = cn - 1
        barr[ci][cj] = 1    # 대표자는 1의 값을 가짐
        food = farr[ci][cj]

        while True:         # 범위내, 간절함이 0이 아닌 동안
            ci, cj = ci+ di, cj + dj
            if not (0 <= ci< N and 0<= cj < N) or score <= 0:
                break

            if farr[ci][cj] != food: # 전파 진행
                moved.add((ci, cj))     # 전파 당함

                if score > barr[ci][cj] :   #강한 전파
                    farr[ci][cj] = food
                    barr[ci][cj] += 1
                    score -= barr[ci][cj]
                else:                       # 약한 전파
                    farr[ci][cj] |= food     # 비트 연산 or
                    barr[ci][cj] += score
                    break                   # 전파 종료









def myprt():
    for lst in barr:
        print(*lst)
    print('-' * 20)
    for lst in farr:
        print(*lst)
    print('-' * 20)



if __name__ == "__main__":
    N , T = map(int, input().split())

    tbl = { 'T': 4 , 'C': 2, 'M': 1}
    farr = [list(input())for _ in range(N)]
    barr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            farr[i][j] = tbl[farr[i][j]]

    print(farr)


    for i in range(T):
        # [1] 대표자 리스트 (전파 할 우선순위) [우선순위, 신앙심, 행 , 열]
        blst = group()

        myprt()
        # [2] 대표자 리스트 오름차순 정렬 후 전파 진행
        blst.sort()

        move(blst)



        # [3] 매일 저녁 이후 신앙심 출력
        # 민초우(7) , 민초(6) , 민우(5) , 초우(3) , 우유(1) , 초코(2), 민트(4)
        ans = [0] * 7
        for idx, food in enumerate((7,6,5,3,1,2,4)):
            for i in range(N):
                for j in range(N):
                    if farr[i][j] == food:
                        ans[idx] += barr[i][j]

        print(*ans)