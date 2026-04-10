from sympy.codegen.scipy_nodes import cosm1


def rotate(arr, si, sj): # 90도 시계방향 회전
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si + i][sj + j] = arr[si+3-j-1][sj+i]
    return narr
def bfs(arr, v, si, sj, clr):
    q= []
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1
    sset = set()
    sset.add((si, sj))
    cnt+= 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj] == 0 and arr[ni][nj] == arr[ci][cj]:
                q.append((ni, nj))
                v[ni][nj] = 1
                sset.add((ni, nj))
                cnt+= 1

    if cnt >= 3:
        if clr == 1:
            for i, j in sset:
                arr[i][j] = 0
        return cnt
    return 0

def count_clear(arr, clr):
    v = [[0]* 5 for _ in range(5)]

    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                t = bfs(arr,v, i, j, clr)
                cnt += t
    return cnt









K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []

for _ in range(K):
    #[1] 탐사 진행
    mx_cnt = 0
    for rot in range(1, 4):
        for sj in range(3):
            for si in range(3):
                # 회전수 -> 열 -> 행
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                # 유물 개수 카운트
                t = count_clear(narr, 0)  #최대개수
                if mx_cnt < t:
                    mx_cnt = t
                    marr = narr
    # 유물이 없는 경우 턴 즉시 종료
    if mx_cnt == 0: break

    # [2] 연쇄획득
    cnt = 0
    arr = marr
    while True:
        t = count_clear(arr, 1)
        if t==0:
            break # 연쇄획득 종료 => 다음턴으로
        cnt += t

        # arr의 0값인 부분 리스트에서 순서대로 추가
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    ans.append(cnt)
print(*ans)


