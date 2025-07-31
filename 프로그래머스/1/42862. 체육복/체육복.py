def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+2)
    students[0] = 0
    students[-1]= 0
    print(students)
    for i in lost:
        students[i] -= 1
    for j in reserve:
        students[j] += 1
    print(students)
    for i in range(1, n+1):
        if students[i] == 0 :
            if students[i-1] >1 :
                students[i] += 1
                students[i-1] -= 1
            elif students[i+1] >1 :
                students[i] += 1
                students[i+1] -= 1
    zero = students.count(0)
    answer = n - zero +2 
    return answer