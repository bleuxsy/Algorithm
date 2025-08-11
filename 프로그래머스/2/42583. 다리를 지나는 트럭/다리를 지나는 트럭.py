from collections import deque 

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    answer = 0
    pending = deque(truck_weights)
    total_weight = 0
    time = 0
    while bridge:
        time+=1
        total_weight -= bridge.popleft()
        if pending:
            if total_weight + pending[0] <= weight:
                truck = pending.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
    return time 
        # if len(bridge) == bridge_length and sum(bridge) <= weight:
        #     time += 1
        # else:
        #     n = bridge.popleft()
        #     if n == -1:
        #         return time
        #     bridge.appendleft(0)
        #     time += 1
        # bridge.popleft()
        # if pending:
        #     bridge.append(pending.popleft())
        # else:
        #     bridge.append(-1)
    
    #     answer = 0
    
#     for i in range(len(truck_weights)+1):
#         for j in range(i+1, len(truck_weights)+1):
#             if len(truck_weights[i:j]) != bridge_length and sum(truck_weights[i:j]) <= weight:
#                 answer +=1
#             break;
#     if bridge_length <= len(truck_weights) :
#         return answer +bridge_length +2
#     else:
#         return answer + bridge_length
#     return answer