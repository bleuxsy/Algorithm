import sys
from collections import deque
sys.stdin = open("input.txt", "r")




    # 이동 경로 횟수랑 이동 경로 출력.

def find_route(si, sj , ei, ej):
    q = deque()
    v = [[0] *N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = ((si, sj))              # 직전 위치를 저장
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            route = []
            ci, cj = v[ci][cj]
            while (ci, cj) != (si, sj):         #출발지가 아니라면 저장
                route.append((ci, cj))
                ci, cj = v[ci][cj]

            return route[::-1]          #   이동 역순 return

        for di, dj in ((-1, 0), (1, 0) , (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<= ni < N and 0 <= nj <N and v[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = (ci, cj)

    # 이곳까지 왔다는 건 목적지를 못찾음
    return -1
def mark_line(v, ci, cj, dr):
    while 0<= ci < N and 0 <= cj < N:
        v[ci][cj] = 2
        ci, cj = ci+di[dr] , cj + dj[dr]

def make_stone(marr, mi, mj, dr):
    v = [[0]* N for _ in range(N)]
    cnt = 0
    # [1] dr 방향으로 > 0 만날떄까지 1 표시 , 이후 2 표시
    ni, nj = mi+di[dr] , mj + dj[dr]
    while 0<= ni < N and 0<= nj <N:
        v[ni][nj] = 1
        if marr[ni][nj] > 0:
            cnt += marr[ni][nj]
            ni , nj = ni + di[dr], nj + dj[dr]
            mark_line(v, ni, nj, dr)
            break
        ni, nj = ni + di[dr] , nj + dj[dr]

    #[2] dr-1 , dr+1 방향으로 동일처리, 대각선 원점 잡고 dr 방향 처리
    for org_dr in ((dr-1)% 8, (dr+1)% 8):
        si, sj = mi+di[org_dr], mj + dj[org_dr]
        while 0<= si< N and 0<= sj < N:
            if v[si][sj] == 0 and marr[si][sj] > 0:
                v[si][sj] = 1
                cnt += marr[si][sj]
                mark_safe(v, si)
if __name__ == "__main__":

    N , M = map(int, input().split())
    si, sj, ei, ej = map(int, input().split())
    men = []
    tlst = list(map(int,input().split()))
    for i in range(0, M*2, 2):
        men.append([tlst[i], tlst[i+1]])
    arr = [ list(map(int, input().split())) for _ in range(N)]

    # [1] 메두사의 이동 : 최단 경로 (상하좌우) -> BFS 경로
    # 메두사의 최단 경로 구하기
    route = find_route(si, sj, ei, ej)
    print(route)
    if route == -1:
        print(-1)
    else:
        for mi , mj in route:
            move_cnt , attk_cnt = 0 , 0
            ## 메두사 이동 : 지정된 최단 거리로 한 칸 이동
            for i in range(len(men)-1, -1, -1):     #삭제할 때는 역순으로 하는게 편리함
                if men[i] == [mi, mj]:
                    men.pop(i)

        di = [-1, -1, 0, 1, 1, 1, 0, -1]
        dj = [0, 1, 1, 1, 0, -1, -1, -1]

        # marr[][] : 지도에 있는 전사 수
        marr = [[0]* N for _ in range(N)]
        for ti, tj in men:
            marr[ti][tj] += 1

        mx_stone = -1
        v= []
        ## 메두사의 시선 -> 가장 많이 돌로 만들 수 있는 방향으로
        for dr in (0, 4, 6, 2):         #상하좌우 순서로 처리
            tv , tstone = make_stone(marr, mi, mj, dr)
            if mx_stone < tstone :
                mx_stone= tstone
                v = tv
        print(move_cnt, mx_stone, attk_cnt)
        print(0)