#11
def solution(s):
  stack =[]
  for c in s:
    if stack and stack[-1]==c:
      stack.pop
    else:
      stack.append(c)
  return int(not stack)

@12
def solution(prices):
  n = len(prices)
  answer = [0] * n 

 
  stack = [0] 
  for i in range(1, n):
    while stack and prices[i] < prices[stack[-1]]:
      j = stack.pop( ) 
      answer[j] = i - j
    stack.append(i)
  while stack:
    j = stack.pop( ) 
    answer[j] = n - 1 - j
  return answer 
