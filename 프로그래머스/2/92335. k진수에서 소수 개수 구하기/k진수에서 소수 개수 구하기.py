from collections import deque
def isprime (num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # √n까지만 체크
        if num % i == 0:
            return False
    return True
def toK (n , k):
    stack = ''
    while n > 0 :
        stack+=str(n % k)
        n = n//k
    return stack 
    
def solution(n, k):
    answer = 0
    prime = ''
    prime = toK(n, k)
    prime = prime[::-1]
    dq = list( prime.split("0"))
    for i in dq:
        if i == '':
            continue
        if isprime(int(i)):
            answer += 1

    return answer