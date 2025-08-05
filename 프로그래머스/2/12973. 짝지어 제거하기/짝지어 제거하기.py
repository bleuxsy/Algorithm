from collections import deque
def solution(s):
    answer = -1
    stack = []
    for word in s:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    if stack : 
        return 0
    return 1