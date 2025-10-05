# def solution(cap, n, deliveries, pickups):
#     path = 0
    
#     for i in range(n-1, -1 , -1): 
#         now = cap
#         ### 배달 갈때
#         if 0 < deliveries[i]  :
#             path += (i+1)
#             k = i
#             while now > 0: 
#                 if k < 0:
#                     break
#                 a =  min(deliveries[k], now)
#                 now -= a
#                 deliveries[k] -= a
#                 k -= 1
#         print(i)
#         print(deliveries)
#         if 0 < pickups[i]:
#             path += (i+1)
#             l = i
#             while now < cap:
#                 if l < 0:
#                     break
#                 m = min(pickups[l], cap-now)
#                 now += m
#                 pickups[l] -= m
#                 l -= 1
#             print(pickups)
            
#     answer = -1
#     print(f"path : {path}")
#     return path

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_remain, p_remain = 0, 0  # 남은 배달, 수거량
    
    for i in range(n-1, -1, -1):  # 가장 먼 집부터 처리
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        # 해당 위치에서 아직 처리해야 할 물량이 있으면
        while d_remain > 0 or p_remain > 0:
            d_remain -= cap
            p_remain -= cap
            answer += (i+1) * 2  # 왕복 거리 추가
    
    return answer