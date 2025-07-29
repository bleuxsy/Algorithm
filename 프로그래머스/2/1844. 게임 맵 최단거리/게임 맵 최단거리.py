from collections import deque 
def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
        
    def dfs(x,y):
        
        stack = deque([(x,y)])
        while stack :
            x, y = stack.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1: 
                    maps[nx][ny]= maps[x][y] + 1
                    stack.append((nx,ny))
                else: continue
        return maps[len(maps)-1][len(maps[0])-1]
    answer = dfs(0,0)
    return -1 if answer == 1 else answer
        # while stack:
        #     node = stack.popleft()
        #     if maps[node[0]][node[1]] == 1 and visited[node[0][node[1]]] = False:
        #         answer
        #         vistied[node[0][node[1]]] = True
        #         stack.append([node[0]+1 , node[1]], 
        #                      [node[0], node[1]+1], 
        #                      [node[0]-1 , node[1] ], 
        #                      [node[0], node[1]-1]) 
        #     else: continue

    #     while stack:
    #         node = stack.popleft()
    #         if maps[node[0]][node[1]] == 1 and visited[node[0]][node[1]] == False:
    #             visited[node[0]][node[1]] = True


    #     visited = [ False * 5  for i in range(5)  ]
    #     for node in stack:
    #         if visited[node[0]][node[1]] == False:
    #             stack.append([node[0], node[1]])

    #     for i in range(5):
    #         for j in range(5):
    #             if maps[i][j] != 1:
    #                 continue;
    #             if i < 0 or j < 0 or i>5 of j > 5: 
    #                 continue;
    #             stack.append([i, j])


    
    return answer