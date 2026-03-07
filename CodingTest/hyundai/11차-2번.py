from collections import deque

N,K = map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

cells=[]
for i in range(N):
    for j in range(N):
        cells.append((grid[i][j],i,j))

cells.sort()

def possible(limit):

    dp=[[1]*N for _ in range(N)]

    for h,x,y in cells:

        for d in range(4):

            nx=x+dx[d]
            ny=y+dy[d]

            if 0<=nx<N and 0<=ny<N:

                if grid[nx][ny]>grid[x][y]:

                    diff=grid[nx][ny]-grid[x][y]

                    if diff<=limit:

                        dp[nx][ny]=max(dp[nx][ny],dp[x][y]+1)

                        if dp[nx][ny]>=K:
                            return True

    return False


lo,hi=0,10**9
ans=-1

while lo<=hi:

    mid=(lo+hi)//2

    if possible(mid):
        ans=mid
        hi=mid-1
    else:
        lo=mid+1

print(ans)