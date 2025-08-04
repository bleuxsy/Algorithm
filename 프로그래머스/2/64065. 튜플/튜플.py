def solution(s):
    answer = []
    
    arr = list(s.split("},{"))
    arr[0] = arr[0][2:]
    arr[-1] = arr[-1][:-2:]
    arr = [list(map(int, a.split(","))) for a in arr]

    
    
    arr.sort(key=lambda x: len(x))
    for a in arr:
        for num in a:
            if num not in answer:
                answer.append(num)
    
    return answer