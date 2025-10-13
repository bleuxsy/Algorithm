def solution(name):
    answer = 0
    total = 0
    stack = [0] * len(name)
    start = 'A' * len(name)
    total = len(name) - 1
    names = []
    for i , char in enumerate(name):
        answer += min(ord(char)-ord('A'), ord('Z') - ord(char) + 1)
        next = i +1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        total = min([total, i*2 + len(name) - next, i+ 2*(len(name)- next)])
    
    answer += total
    return answer