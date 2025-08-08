def solution(friends, gifts):
    answer = 0
    rel = [[0] * len(friends) for _ in range(len(friends))]
    score = [0] * len(friends)
    newgift = [0] * len(friends)
    for i in gifts:
        A , B = i.split(" ")
        rel[friends.index(A)][friends.index(B)] += 1
    for i in range(len(rel)):
        score[i] += sum(rel[i])
    for i in range(len(rel)):
        for j in range(len(rel)):
            score[i] -= rel[j][i]
    print(score)
    for i in range(len(rel)):
        for j in range(i+1, len(rel)):
            if rel[i][j] < rel[j][i]:
                newgift[j] += 1
            elif rel[i][j] > rel[j][i]:
                newgift[i] += 1
            else:
                if score[i] > score[j]:
                    newgift[i] +=1
                elif score[i] < score[j]:
                    newgift[j] += 1
    
                    
    answer = max(newgift)               
    return answer