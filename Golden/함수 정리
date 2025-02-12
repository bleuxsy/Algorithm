def solution(numbers):
    ret = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            ret.append(numbers[i]+numbers[j])
    ret = sorted(set(ret))
    return ret
            
def solution(answers):
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    scores =[0] *3
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
