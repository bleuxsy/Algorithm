def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5,]
    
    dic = { i : 0 for i in range(1,4)}
    
    for i in range(len(answers)):
        
        if p1[i % 5] == answers[i]:
            dic[1] += 1
        if p2[i%8] == answers[i]:
            dic[2] += 1
        if p3[i%10] == answers[i]:
            dic[3] += 1
    sorted(dic.values())
    maxscore = max(dic.values())
    print(maxscore)
    for i in range(1,4):
        if maxscore == dic[i]:
            answer.append(i)
    return answer