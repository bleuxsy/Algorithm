def solution(survey, choices):
    answer = ''
    char = [ 'R', 'T', 'C', 'F', 'J' , 'M' , 'A' , 'N']
    score = [0] * 8
    for i in range(len(survey)):
        if choices[i] >=4 :
            score[char.index(survey[i][1])] += (choices[i] - 4)
        else:
            score[char.index(survey[i][0])] += (4 - choices[i] )
    print(score)
    for i in range(0, 7, 2):
        if score[i] > score[i+1]:
        
            answer += (char[i])
        elif score[i] < score [i+1]:
            
            answer +=(char[i+1])
        else:
            answer+=(min(char[i] , char[i+1]))
    return answer