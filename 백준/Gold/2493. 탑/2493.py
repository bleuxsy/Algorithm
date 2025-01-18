N = int(input())
tower = list(map(int, input().split()))
laser = []
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            laser.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        laser.append(0)
    stack.append([i, tower[i]])
for i in laser:
    print(i)






# for i in reversed(range(N)):
#     for j in range(1, i+1):
#         if tower[i] <= tower[i-j]:
#             laser[i] = i-j+1
#             break
#
# for i in laser:
#     print(i)



