def solution(number, k):
    stack = []
    for ch in number:
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)


    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
# def back(lst, idx):
#     if len(lst) == n:
#         answer.append(int(''.join(lst)))
#         return
#     for j in range(idx, len(num)):
#         lst.append(num[j])
#         back(lst, j + 1)
#         lst.pop()

# def solution(number, k):
#     global answer, num, n
#     answer = []
#     num = list(number)
#     n = len(num) - k

#     back([], 0)
#     print(answer)
    
#     return str(max(answer))
