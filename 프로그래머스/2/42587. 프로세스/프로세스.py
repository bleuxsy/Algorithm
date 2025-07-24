from collections import deque
def solution(priorities, location):
    h = len(priorities)
    answer = 0

    queue = [[i,p] for i,p in enumerate(priorities)]
    print(queue)
    while True:
        now = queue.pop(0)
        if any(now[1] < other[1] for other in queue ):
            queue.append(now)
        else:
            answer += 1
            if now[0] == location:
                return answer
    # for i in range(h):
    #     dq.append(i)
    # print(dq)
    # for i in range(h):
    #      if any(priorities[dq[0]] < priorities[other] for other in range(dq[1], len(dq))):
    #             now = dq.popleft()
    #             dq.append(now) 
    # print(dq)
    # answer = dq.index(location) +1
    
    