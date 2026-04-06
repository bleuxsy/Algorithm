import sys
from collections import deque


sys.stdin = open("input.txt", "r")

def myprint(arr):
    for lst in arr:
        print(*lst)
    print()
def find_route(si, sj, ei, ej):
    q = deque()
    v = [[0] * N for _ in range(N)]

    q.append((si, sj))

    v[si][sj] = ((si,sj)) # 직전 위치를 저장

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            route = []
            ci, cj = v[ci][cj]
            while (ci, cj) != (si, sj):
                route.append((ci, cj))
                ci, cj = v[ci][cj]
            return route[::-1]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni <N and 0 <=nj <N  and v[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = (ci, cj)
    return -1
def mark_line(v , ci, cj , dr):
    while 0<= ci < N and 0<= cj < N:
        v[ci][cj] = 2
        ci, cj = ci+di[dr] , cj+dj[dr]
def mark_safe(v, si, sj, dr, org_dr):
    ci , cj = si+di[dr], sj+dj[dr]
    mark_line(v,ci,cj, dr)

    ci, cj = si+di[org_dr], sj+dj[org_dr]
    while 0<=ci< N and 0<=cj<N:
        mark_line(v,ci, cj, dr)
        ci, cj = ci+di[org_dr], cj+dj[org_dr]
def make_stone(marr, mi, mj, dr):
    # [1] dr 방향으로 > 0 만날때까지 1 표시, 그 후 2 표시
    v = [[0]*N for _ in range(N)]
    cnt = 0

    ni, nj = mi+di[dr], mj+dj[dr]
    while 0<=ni<N and 0<=nj<N:
        v[ni][nj] =1
        if marr[ni][nj] > 0:
            cnt += marr[ni][nj]
            ni, nj = ni + di[dr], nj + dj[dr]
            mark_line(v, ni, nj, dr)
            break
        ni, nj = ni+di[dr], nj+dj[dr]
    # [2] dr-1 , dr+1 방향으로 이동 후 다시 직선
    for org_dr in ((dr-1)%8 , (dr+1)%8):
        si, sj = mi+di[org_dr], mj+dj[org_dr]
        while 0<=si<N and 0<=sj<N:
            # 대각선으로
            if v[si][sj]==0 and marr[si][sj] >0:
                v[si][sj] = 1
                cnt+= marr[si][sj]
                mark_safe(v, si, sj, dr, org_dr)
                break
            # 직선으로
            ci, cj = si, sj
            while 0<= ci < N and 0<= cj < N:
                if v[ci][cj] == 0:
                    v[ci][cj] = 1
                    if marr[ci][cj] > 0:
                        cnt += marr[ci][cj]
                        mark_safe(v, ci, cj, dr, org_dr)
                        break
                else:
                    break
                ci, cj = ci+di[dr], cj+dj[dr]

            si, sj = si+di[org_dr], sj+dj[org_dr]
    return v, cnt
def move_men(v, mi, mj):
    #메두사 시야가 아니면 이동 가능 상하좌우, 좌우상하
    move, attk = 0, 0
    for dirs in (((-1,0), (1,0), (0,-1), (0,1)), ((0,-1), (0, 1), (-1, 0), (1, 0)) ):
        for idx in range(len(men)-1, -1, -1):
            ci, cj = men[idx]
            if v[ci][cj] == 1:
                continue
            dist = abs(mi-ci)+ abs(mj-cj)
            for di, dj in dirs:
                ni, nj = ci+di, cj+dj
                if 0<= ni < N and 0<= nj< N and v[ni][nj] != 1 and dist> abs(mi-ni) + abs(mj-nj):
                    if (ni, nj) == (mi, mj):
                        attk+= 1
                        men.pop(idx)
                    else:
                        men[idx] = [ni, nj]
                    move+=1
                    break

    return move, attk
if __name__ == "__main__":
    N, M = map(int, input().split())
    si, sj, ei, ej = map(int, input().split())
    tlst = list(map(int, input().split()))

    men = []

    for i in range(0, M*2 , 2):
        men.append([tlst[i], tlst[i+1]])
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [0] BFS로 메두사 최단 경로

    route = find_route(si, sj, ei, ej)
    print(route)
    if route == -1:
        print(-1)
    #
    else:
        for mi , mj in route:
            move_cnt, attk_cnt = 0, 0
            # [1] 메두사의 이동: 지정된 최단 거리로 한 칸 이동
            # 삭제할때는 뒤에서 부터 오면서 삭제하는 게 제일 베스트
            for i in range(len(men)-1, -1, -1):
                if men[i] == [mi, mj]:
                    men.pop(i)

            di = [-1,-1,0,1,1,1,0,-1]
            dj = [0,1,1,1,0,-1,-1,-1]
            # marr[][] : 지도에 있는 전사수
            marr = [[0]*N for _ in range(N)]
            for ti, tj in men:
                marr[ti][tj] += 1

            # [2] 메두사의 시선
            # => v[]에 표시해서  이동시 참조 (메두사 시선 ==1 , 가려진 곳== 2 , 빈땅 == 0)
            mx_stone = -1
            v = []
            for dr in (0, 4, 6, 2): #상하좌우
                    tv, tstone = make_stone(marr, mi,mj, dr)

                    if mx_stone < tstone:
                        mx_stone = tstone
                        v = tv



            # [3] 전사들의 이동
            move_cnt, attk_cnt = move_men(v, mi,mj)
            print(move_cnt, mx_stone, attk_cnt)
        print(0)