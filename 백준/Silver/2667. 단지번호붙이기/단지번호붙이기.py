from collections import deque
stack = deque()
count = 0
def dfs(x,y):
    global count
    dx = [ 1 , 0, -1, 0]
    dy = [ 0 , 1,  0,-1]
    if x < 0 or x>= N or y <0 or y >= N:
        return
    if grid[x][y] == 1 :
        grid[x][y] = 0
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

N = int(input())
grid = [list(map(int, input())) for i in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            dfs(i,j)
            answer.append(count)
            count = 0
answer.sort()
print(len(answer))
for i in answer:
    print(i)
