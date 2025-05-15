def dfs(i, total):
    global answer
    if i == len(numbers):
        if total == target:
            answer += 1
        return
    dfs(i + 1, total + numbers[i])
    dfs(i + 1, total - numbers[i])

def solution(nums, tgt):
    global numbers, target, answer
    numbers = nums
    target = tgt
    answer = 0
    
    dfs(0, 0)
    return answer