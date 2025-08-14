from collections import deque
def solution(k, dungeons):
    global visited, answer
    answer = 0
    visited = [False] * (len(dungeons))
    dfs(k,0, dungeons)
    return answer

def dfs (k, n , dungeons):
    global answer
    if n > answer :
        answer= n
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= k:
            visited[i] = True
            dfs(k-dungeons[i][1], n+1 , dungeons)
            visited[i] = False
    
#     stack = deque(dungeons)
    
#     dungeons.sort(key = lambda x :-(x[0]-x[1]))
#     for i in range(len(dungeons)):
#         if dungeons[i][0] <= k :
#             answer +=1
#             k -= dungeons[i][1]
#     print(answer)
#     visited = [False] * 3
#     for i in range(len(dungeons)):
#         visited[i] = True
#         now = dungeons
#         start , need = dungeons[i][0] , dungeons[i][1]
#         sol(k,start,need, dungeons, visited)
#         vistied[i] = False
#     print(dungeons)

