#문제8

def solution():
    words = input()
    stack =[]
    for word in words:
        if word == "(":
            stack.append(word)
        elif word == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack :
        return False
    else:
        return True    
    
#문제 9
def solution(N):
    stack = []
    while N >0:
        stack.append(str(N%2))
        N //= 2
    binary = ""
    while stack:
        binary+= stack.pop()
    return binary    
