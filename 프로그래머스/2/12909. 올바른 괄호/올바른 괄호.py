def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) == 0 :
            if i == '(':
                stack.append(i)
            else:
                return False
        elif i == '(':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
    if len(stack) != 0:
        return False
    return True