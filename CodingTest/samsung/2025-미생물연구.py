from collections import deque
def bfs(v, si, sj):
    q = deque()
    sn = arr[si][sj]
    rlst = []

    q.append((si,sj))
    v[si][sj]=sn
    rlst.append(sn)
    rlst.append([si,sj])

    while q:
        ci,cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(같은 값이면==sn)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==sn:
                q.append((ni,nj))
                v[ni][nj]=sn
                rlst.append([ni,nj])
    return rlst

def group():
    v = [[0]*N for _ in range(N)]
    glst = []

    for si in range(N):
        for sj in range(N):
            # 미방문 미생물이면 그루핑
            if v[si][sj]==0 and arr[si][sj]>0:
                tlst = bfs(v, si, sj)
                glst.append(tlst)

    # glst = [미생물번호, [i1, j1], [i2, j2]..]
    return glst

def arr_input():
    sj,si,ej,ei = map(int, input().split())
    for i in range(si,ei):
        for j in range(sj,ej):
            arr[i][j]=n

def del_sort(glst):
    del_set = set()                     # 삭제할 그룹 인덱스
    for i in range(len(glst)-1):
        for j in range(i+1, len(glst)): # 가능한 2개를 선택하는 모든 조합
            if glst[i][0]==glst[j][0]:  # 같은 미생물 번호를 가진 그룹이면(분리된 그룹)
                del_set.add(i)
                del_set.add(j)

    for i in range(len(glst)-1,-1,-1):  # 삭제는 뒤부터
        if i in del_set:
            glst.pop(i)                 # 삭제

    # 정렬(크기 큰 -> 오랜된(미생물번호 작은)
    glst.sort(key=lambda x: (-len(x),x[0]))

    # 그룹내 좌표를 (0,0)기준의 상대좌표로 저장
    for lst in glst:
        # i, j 최소값 구하기(si,sj) => 모든좌표에서 -si, -sj
        si, sj = N, N
        for ci,cj in lst[1:]:           # lst[0]은 미생물번호
            si = min(si, ci)
            sj = min(sj, cj)

        for idx in range(1,len(lst)):   # 모든 좌료플 (0,0)기준 상대좌표로 저장
            lst[idx][0]-=si
            lst[idx][1]-=sj

    return glst

def check(arr, lst):
    # 최소열/최소행 기준으로 배치가능한지 체크후 기준좌표 리턴(불가능시 (-1,-1)리턴
    for sj in range(N):
        for si in range(N):         # 가능한 모든 기준위치
            # 기준(si,sj)에 더한 모든좌표가 범위내이고 0이면 성공
            for ci,cj in lst:
                if si+ci>=N or sj+cj>=N or arr[si+ci][sj+cj]!=0:
                    break
            else:                   # 모든 좌표 배치가능
                return si,sj
    # 가능한 기준좌표 없음
    return -1,-1

def move(glst):
    narr = [[0]*N for _ in range(N)]

    for lst in glst:                # 한 그룹씩 배치가능한 최소위치(si,sj)에 배치
        sn = lst[0]
        si,sj = check(narr, lst[1:]) # 가능한 시작좌표 리턴, 불가능한 경우 (-1,-1)리턴
        if (si,sj) != (-1,-1):
            for ci,cj in lst[1:]:
                narr[si+ci][sj+cj]=sn

    return narr

def bfs_adj(v, si, sj):
    # 같은 값일때 그 개수 세고 리턴
    q = deque()

    q.append((si,sj))
    v[si][sj]=1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(같은 값)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[si][sj]==arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt


# 내 그룹개수를 세고(mycnt), 인접한 다른 블럭들 카운트(cnts)구해서 곱해서 누적
def bfs_score(v, si, sj):
    q = deque()
    w = [[0]*N for _ in range(N)]
    cnts = []

    q.append((si,sj))
    v[si][sj]=1
    mycnt = 1

    while q:
        ci,cj = q.popleft()
        # 네방향, 범위내, 미방문
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                if arr[ni][nj]==arr[si][sj]:   # 같은 세포면 mycnt세기
                    q.append((ni,nj))
                    v[ni][nj]=1
                    mycnt+=1

                # 다른세포면: 첫 발견시 그 세포의 개수세기(방문표시w)
                elif arr[ni][nj]>0 and w[ni][nj]==0:
                    tcnt = bfs_adj(w,ni,nj)
                    cnts.append(tcnt)

    ans = 0
    for cnt in cnts:
        ans += mycnt*cnt
    return ans

def score(arr):
    v = [[0]*N for _ in range(N)]
    ans = 0

    for si in range(N):
        for sj in range(N):
            # 미방문 세포 만나면 점수 계산
            if v[si][sj]==0 and arr[si][sj]>0:
                t = bfs_score(v,si,sj)
                ans+=t
    return ans

############################################
# 15
N, Q = map(int, input().split())
arr = [[0]*N for _ in range(N)]

for n in range(1,Q+1):
    # [1] 입력: 기존미생물 덮어씀
    arr_input()

    # [2] 그룹나누기: glst = [미생물번호, [i1,j1],[i2,j2].. ]
    glst = group()

    # [3] 쪼개진개체 삭제 및 정렬(크기, 오래된: 미생물번호 작은)
    glst = del_sort(glst)

    # [4] 큰것/오래된것 부터 이미 정렬된 그룹 이동(재배치)
    arr = move(glst)

    # [5] 점수계산
    ans = score(arr)

    print(ans)

