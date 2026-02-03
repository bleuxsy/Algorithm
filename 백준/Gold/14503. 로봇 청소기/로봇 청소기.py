from collections import deque
N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [ list(map(int , input().split())) for _ in range(N)]
dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1 ]
cleaned = 0

while True:
    ## 청소 되지 않은 경우,
    if grid[r][c] == 0:
        grid[r][c] = 2
        cleaned += 1
    ### 주변 4칸 확인
    moved = False
    for _ in range(4):
        d= (d+3)%4
        nx = r+ dx[d]
        ny = c+ dy[d]

        if grid[nx][ny] == 0 :
            r, c = nx, ny
            moved = True
            break

    if not moved:
        back_d =(d+2)%4
        br = r + dx[back_d]
        bc = c + dy[back_d]

        if grid[br][bc] == 1:
            break
        else:
            r, c  = br, bc
print(cleaned)

