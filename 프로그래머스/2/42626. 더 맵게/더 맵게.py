# def minmax (scoville, K):
#     return all(s >= K for s in scoville)
import heapq 
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_one = heapq.heappop(scoville)
        if min_one >= K:
            break;
        if len(scoville) == 0: 
            return -1
        min_two = heapq.heappop(scoville)
        mixx = min_one + min_two*2
        answer += 1
        heapq.heappush(scoville, mixx)
        
    
    return answer
    # while not minmax(scoville, K):
    #     if len(scoville) < 2:
    #         return -1
    #     scoville = sorted(scoville, reverse=True)
    #     print(scoville)
    #     min_one = scoville.pop()
    #     min_two = scoville.pop()
    #     mixx = min_one + min_two *2
    #     scoville.append(mixx)
    #     print(scoville)
    #     answer += 1
    #     print(answer)
    return answer