N = int(input())
building = [int(input()) for i in range(N)]
seek = []
stack = []
count = 0
for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()
    stack.append(building[i])
    count += len(stack) - 1
print(count)
# for i in range(N):
#     stack.append([i, building[i]])
#     for j in range(i+1, N):
#         if stack[-1][1] > building[j]:
#             count += 1
#         else:
#             stack.pop()
#     count += len(stack) - 1
# print(count)