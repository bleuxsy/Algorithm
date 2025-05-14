def solution(nums):
    length = 0
    length = len(nums)
    answer = 0
    answer = len(set(nums))
    if answer > length/2:
        answer = length/2
    return answer