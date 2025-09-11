from collections import deque

def right(circle):
    circle.appendleft(circle.pop())

def left(circle):
    circle.append(circle.popleft())

circles = [deque(list(map(int, input().strip()))) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    rotate_dir = [0] * 4  # 각 톱니 회전 방향 저장
    rotate_dir[num-1] = dir


    now_dir = dir
    for i in range(num-1, 0, -1):
        if circles[i][6] != circles[i-1][2]:
            now_dir *= -1
            rotate_dir[i-1] = now_dir
        else:
            break


    now_dir = dir
    for i in range(num-1, 3):
        if circles[i][2] != circles[i+1][6]:
            now_dir *= -1
            rotate_dir[i+1] = now_dir
        else:
            break


    for i in range(4):
        if rotate_dir[i] == 1:
            right(circles[i])
        elif rotate_dir[i] == -1:
            left(circles[i])


answer = 0
if circles[0][0] == 1:
    answer += 1
for i in range(1, 4):
    if circles[i][0] == 1:
        answer += pow(2, i)
print(answer)