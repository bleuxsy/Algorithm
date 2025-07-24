def solution(array, commands):
    answer = []
    arry = []
    for i in range(len(commands)):
        arry = array[commands[i][0]-1: commands[i][1]]
        arry = sorted(arry)
        num = arry[commands[i][2]-1]
        answer.append(num)
    
    return answer


