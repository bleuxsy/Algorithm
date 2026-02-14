import sys
sys.stdin = open("input.txt", "r")
from collections import deque
def myprint():
    print("----마을 출력----")
    for row in grid:
        print(row)
    print("--------")


def solve():
    print("계산 들어가자")
    return 0
def go_monster():
    print("정령 움직인다.")

def can_go(gollem, mi, mj):

    for s in range(2, len(gollem) - 1):
        si = gollem[s][0]
        sj = gollem[s][1]
            # 앞으로 갈 곳? 이 비었나...
        ci, cj = si + mi, sj + mj

        if 0 <= ci < R + 3 and 0 <= cj < C and grid[ci][cj] == 0:
            continue
        else:
            # 다음 방향 확인
            return False
    return True
def go_gollem(ci, di):
    print("골렘 들어간다..")
    #골렘 초기 좌표 값  [ 출구, [중앙] , [서쪽] , [동쪽], [남쪽] , [북쪽] ]
    gollem = [[], [1, ci-1], [ 1, ci-2] , [1, ci], [2, ci-1], [0, ci-1]]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for g in gollem[1:]:
        si, sj = g[0] ,g[1]
        grid[si][sj] = 1
    (i, j) = dirs[di]
    m, n = gollem[1]
    gollem[0].append([m+i , n+j])
    grid[m + i][n + j] = 2
    myprint()

    ## 골렘이 이동하는 방향
    moved = ((1, 0), (0, -1), (0, 1))

    # for mi, mj in moved:
    #     if can_go(gollem, mi, mj):
    #         for g in gollem[1:]:
    #             si, sj = g[0] , g[1]
    #             grid[si+mi][sj+mj] = 1
    #             grid[si][sj] = 0

    flag = 1
    while flag != 0:
        mi , mj = moved[1]
        ##남쪽으로 이동
        for i, j in gollem:
            ni = i+ mi
            nj = j + mj
            # 벽에 부딪히면
            if ni == R+2 :
                flag = 0
            #벽이 없으면
            if grid[ni][nj] != 0:
                for di, dj in ((-1,0), (1, 0)):
                    
                    grid[ni][nj] = 1
                    grid[i][j] = 0













if __name__ == "__main__":
    glist = []
    R, C , K = map(int, input().split())
    for i in range(K):
        c, d = map(int, input().split())
        glist.append([c, d])

    # 마을 만들기
    grid = [ [0] * C for _ in range(R+3)]

    answer = 0
    for k in range(K):
        ci, di = glist[k]
        # [1] 골렘 이동
        go_gollem(ci, di)

        # [2] 정령 이동
        go_monster()

        # [3] 최종 위치 합 계산
        res = solve()
        answer += res
    print(answer)
