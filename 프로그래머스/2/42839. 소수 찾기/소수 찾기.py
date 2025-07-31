from itertools import permutations
from collections import deque

def findnum(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def makenum (t):
    new = []
    for i in range(1,len(t)+1):
        for p in permutations(t, i):
                   new.append(''.join(p))
    print(new)
    return new
 
def solution(numbers):
    answer = 0
    #num = list(map(str, numbers))
    #print(num)
    num = makenum(numbers)
    num = set(map(int, num))
    print(num)
    for i in num:
        if findnum(i):
            answer += 1
        
    return answer