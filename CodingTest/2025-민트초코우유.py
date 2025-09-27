from collections import deque
import sys
sys.stdin = open("input.txt", "r")
def sort_word():
    for i in range(len(flist)):
        for j in range(len(flist)):
            word = flist[i][j]
            sw = "".join(sorted(word, reverse = True))
            flist[i][j] = sw




def morning():
    print("아침")
    for i in range(len(blist)):
        for j in range(len(blist)):
            blist[i][j] += 1

def bfs_group(v, si, sj):
    stack= deque()
    rlist = []
    rlist.append(flist[si][sj])
    rlist.append([si, sj])
    v[si][sj] = True
    stack.append((si, sj))

    while stack:
        ci, cj = stack.pop()
        for di , dj in ((-1, 0), (0 , -1), (1 , 0), (0 , 1)):
            ni , nj = ci + di , cj + dj

            if 0<= ni <N and 0<= nj< N :
                if not v[ni][nj]:
                    if flist[ni][nj] == flist[si][sj]:
                        v[ni][nj] = True
                        rlist.append([ni, nj])
                        stack.append((ni, nj))

    return rlist


def group():
    global glist
    print("점심")
    v = [[False] * N for _ in range(N)]
    glist = []
    for si in range(N):
        for sj in range(N):
            if not v[si][sj]:
                mlist =bfs_group(v , si, sj)

                glist.append(mlist)

    return glist
def del_num():

    for i in range(len(blist)):
        for j in range(len(blist)):
            blist[i][j] -= 1

    for i in range(len(olist)):
        x = olist[i][1]
        y = olist[i][2]

        blist[x][y] += len(glist[i]) - 1
        olist[i][0] = blist[x][y]

    print("del적용 후")
    for b in blist:
        print(b)


    return olist



def owner(glist):
    global olist
    olist = []

    idx = 0
    for lst in glist:

        r, c = lst[1][0] , lst[1][1]
        for k in range(2 , len(lst)):
            i = lst[k][0]
            j = lst[k][1]
            if blist[i][j] > blist[r][c]:
                r = i
                c = j
        olist.append([blist[r][c], r,c])
        print(olist)


    olist = del_num()



    return olist
def overdose(o):
    # 전파
    v = [[False] * N for _ in range(N)]
    mov = 0
    d = [[-1, 0] , [1, 0] , [0 , -1], [0 , 1]]

    for i in o:
        mov = i[0] % 4
        stack = deque()
        # 간절함 x = B - 1

        x = i[0] - 1
        ssx = i[1]
        ssy = i[2]
        print("=======")
        print(f"대표 {ssx} {ssy}")
        if v[ssx][ssy]:
            print("break!")
            break
        stack.append([ssx, ssy])
        while stack:
            sx , sy = stack.pop()
            print(f"시작점 {sx} {sy}")
            # if v[sx][sy] :
            #     print("break!")
            #     break
            nx = sx + d[mov][0]
            ny = sy + d[mov][1]
            print("다음 좌표")
            print(nx, ny)
            if 0<= nx < N and 0 <= ny < N and x > 0:

                if flist[nx][ny] == flist[ssx][ssy]:
                    print(f"{nx} {ny} pass")
                    i[0] = 1
                    blist[ssx][ssy] = 1
                    stack.append([nx, ny])
                    print(f"다음 {stack}")
                else:
                    v[nx][ny] = True

                    #신봉 음식이 다른 경우에는 전파가 진행이 됨
                    print(f"전파 시작 {nx} {ny}")
                    y = blist[nx][ny]
                    blist[ssx][ssy] = 1
                    # 강한 전파
                    if y < x:
                        print("강한 전파")
                        flist[nx][ny] = flist[ssx][ssy]

                        x -= (y+1)
                        blist[nx][ny] += 1
                        for f in flist:
                            print(f)
                        for b in blist:
                            print(b)
                        stack.append([nx,ny])
                        print(stack)
                        if x == 0:
                            break
                    else:
                        #약한 전파
                        print("약한 전파")
                        print(x)
                        blist[nx][ny] += x
                        flist[nx][ny] += flist[ssx][ssy]
                        for f in flist:
                            print(f)
                        for b in blist:
                            print(b)

                        x = 0
                        break
    print("==============")
    return

def lunch():

    glist = group()
    o = owner(glist)

    print(f"대표자 {o}")

    return o
def evening(o):

    o.sort(key=lambda x: (-x[0], x[1], x[2]))
    print(f"저녁에 순서 {o} 정렬")
    overdose(o)
    print("저녁 이후 flist, blist")
    for F in flist:
        print(F)
    for b in blist:
        print(b)

def solution():
    res = [0] *7

    sort_word()

    for i in range(len(flist)):
        for j in range(len(flist)):
            if len(flist[i][j]) == 3 :
                res[0] += blist[i][j]
            elif  flist[i][j] == "TC":
                res[1] += blist[i][j]
            elif  flist[i][j] == "TM":
                res[2] += blist[i][j]
            elif flist[i][j] == "MC" :
                res[3] += blist[i][j]
            elif flist[i][j] == "M":
                res[4] += blist[i][j]
            elif flist[i][j] == "C":
                res[5] += blist[i][j]
            else:
                res[6] += blist[i][j]
    return res
if __name__ == "__main__":
    N , T = map(int, input().split())
    flist = [list( input()) for _ in range(N)]

    for F in flist:
        print(F)

    blist = [list(map(int, input().split())) for _ in range(N)]
    for b in blist:
        print(b)


    for i in range(2):
        # 1. 아침
        sort_word()
        morning()
        for row in blist:
            print(row)
        for row in flist:
            print(row)
        # 2. 점심
        ownerlist = lunch()
        # 3. 저녁

        evening(ownerlist)

        print(f"#{i+1} {solution()}")
        print("------------next---------------")
        #print(f"#{i} {result}")