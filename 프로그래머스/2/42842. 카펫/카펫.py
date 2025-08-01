from collections import deque 
def solution(brown, yellow):
    answer = []
    res = deque()
    c = 0
    r = 0
    num = brown + yellow
    for i in range(3,(num//2)):
        if num % i == 0:
            c = num//i 
            r = i
            res.append((r,c))
            
    while res:
        r,c = res.popleft()
        if (r-2) * (c-2) == yellow:
            answer.append(max(r,c))
            answer.append(min(r,c))
            print(answer)
            return answer