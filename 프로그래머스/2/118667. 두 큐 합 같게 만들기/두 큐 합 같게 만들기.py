# import queue
from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    answer = 0
    h = len(q1)
    sum1 = sum(q1)
    sum2 = sum(q2)
    limit = h * 3
    while sum1 != sum2:
        if sum1 > sum2 :
            num = q1.popleft()
            q2.append(num)
            
            sum1 -= num
            sum2 += num 
        else :
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num 
        answer += 1
        if answer == limit:
            return -1
    
    return answer
    
    
