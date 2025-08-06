from collections import deque
def solution(n, computers):
    visited = [False] * n
    def dfs(m):
        visited[m] = True
        for i in range(n):
            if not visited[i] and computers[m][i] == 1:
                dfs(i)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer +=1
    return answer
    # answer = 0
    # stack = [0] * n
    # visited = [False]* n
    # for i in range(len(computers)):
    #     for j in range(i+1, len(computers)):
    #         if computers[i][j] == 1 :
    #             stack[i] = j
    # print(stack)
    # def dfs(stack,start,visited):
    #     stack = [start]
    #     while stack:
    #         value = stack.pop()
    #         if not visited[value] and stack[value] != 0:
    #             visited[value] = True
    #             stack.append(stack[value])
    #         elif visited[value] and stack[value] == 0:  
    #             answer += 1
    #         else:
    #             answer +=1
    #     return answer
    # dfs(stack , 0 , visited )
    
