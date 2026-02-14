nums = input()

i = 0
while True:
    i += 1
    n = str(i)

    idx = 0  
    while idx < len(n) and nums:
        if nums[0] == n[idx]:
            nums = nums[1:]
        idx += 1

    if not nums:
        print(i)
        break