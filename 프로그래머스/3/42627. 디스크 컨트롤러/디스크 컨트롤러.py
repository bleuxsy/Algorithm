import heapq;

def solution(jobs):
    answer = 0
    h = []
    i =0 
    jobs.sort()
    now = 0
    start = -1 
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(h, (j[1],j[0]))
            
        if h:
            x , y = heapq.heappop(h)
            start = now
            now += x
            answer += now - y 
            i += 1
        else:
            now += 1
    return answer // len(jobs)
        #time[i] += request + start
       
   