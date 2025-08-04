from collections import deque
from itertools import permutations
def solution(numbers):
    # number = deque()
    answer = ''
    a = deque()
    number = list(map(str, numbers))
    ## permutation의 시간복잡도는 n!
    # arr = list(permutations(number, len(numbers)))
    # for i in arr:
    #     num = ''.join(i)
    #     a.append(num)
    number.sort(key= lambda x : x*3 , reverse = True)
    answer = ('').join(number)
    
    if answer[0] == '0':
        return '0'
    # answer= max(a)
    return answer