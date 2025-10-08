def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    def dfs(sheep , wolf ):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            # 부모는 방문했으나 자식은 방문 안했을떄
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep+1 , wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
    return max(answer)