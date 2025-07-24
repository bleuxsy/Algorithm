import math
def solution(progresses, speeds):
    answer = {}
    answers =[]
    days = []
    for i in range(len(progresses)):
        remain = 100-progresses[i]
        day = math.ceil(remain / speeds[i])
        if len(days) == 0: days.append(day)
        elif len(days) != 0:
            if day < days[-1]:
                day = days[-1]
                days.append(day)
            else: days.append(day)
    for d in days:
        if d in answer:
            answer[d] += 1
        else:
            answer[d] = 1
    answers = list(answer.values())
    return answers

