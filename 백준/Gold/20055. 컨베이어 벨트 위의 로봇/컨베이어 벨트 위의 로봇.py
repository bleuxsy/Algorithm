"""

올리는위치                      내리는 위치
 1     2    3   ....   N-1   N

 2n  2n-1 2n-2               N+1



1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
2. 로봇 순서대로 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동, 이동할 수 없으면 가만히
    - 이동하려는 칸에 로봇이 없어야 하며, 칸의 내구도가 1이상
    - 내리는 위치에 도달하면 로봇은 내림
3. 올리는 위치 (1)에 있는 칸 내구도가 0이 아니면 로봇을 올림
4. 내구도가 0인 칸의 개수가 >= K 면 종료, 그렇지 않으면 1번으로 돌아감


출력
몇 번째 단계가 진행 중일때 종료되었는지 출력
"""
from collections import deque
# 종료 조건
def flag():
    cnt = 0
    for b in a:
        if b == 0:
            cnt += 1

    if cnt >= K:
        return True
    else:
        return False
def rotate():
    # 벨트 회전
    lst = a.pop()
    a.appendleft(lst)

    # 로봇 회전
    robot.pop()
    robot.appendleft(0)
    robot[-1] = 0
    return
def move():

    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and a[i + 1] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            a[i + 1] -= 1


    robot[-1] = 0



    return

def add():
    if a[0] != 0:
        robot[0] = 1
        a[0] -=1

N , K = map(int, input().split())
A = list(map(int, input().split()))
a = deque(A)

robot = deque([0] * N)

step = 0
while True:
    step += 1
    rotate()
    move()
    add()
    if flag():
        print(step)
        break


