def solution(word):
    answer = 0
    stack = []
    def dfs(L, w):

        if L == 5:
            return 
        
        for i in 'AEIOU':
            stack.append(w+i)
            dfs(L+1, w+i)
    dfs(0, '')
    print(stack)
    answer = stack.index(word) + 1
    return answer