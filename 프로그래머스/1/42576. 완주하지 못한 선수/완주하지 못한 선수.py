from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    answer = p_counter - c_counter
    return list(answer.keys())[0]