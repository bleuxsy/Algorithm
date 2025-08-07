from collections import deque
def findword(word1, word2):
    count = 0
    for i, j in zip(word1, word2):
        if i != j :
            count +=1
    if count == 1:
        return True
    return False 
def solution(begin, target, words):
    answer = 0
    start =''
    if target not in words:
        return 0
    start = begin
    visited = [False] * len(words)
    queue = deque([(start , 0)])
    while queue:
        now , cnt = queue.popleft()
        if now == target:
            return cnt
        for i ,word in enumerate(words):
            if not visited[i]  and findword(now, word):
                visited[i] = True
                queue.append((word, cnt + 1))
    return 0
    
            