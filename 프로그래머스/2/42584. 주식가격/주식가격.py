from collections import deque
def solution(prices):
    times = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            times[i] += 1
            if prices[j] < prices[i]:
                break
    return times
# def solution(prices):
#     answer = []
#     times = []
#     for i in range(len(prices)):
#         for j in range(i ,len(prices)+1):
#             if prices[i] <= prices[j]:
#                 times[i] +=1
#             else:
#                 break;
#     return times
    
    # check = deque(prices[0])
    # prices = deque(prices)
    # time = 0
    # prices.popleft()
    # while check:
    #     if check[-1] <= prices[0]:
    #         time +=1
    #         check.append(prices.popleft())
    #     else:
    #         times[len(check)-1] = time
    #         check.pop()
    #         check.append(prices.popleft())
  