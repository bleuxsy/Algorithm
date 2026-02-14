M , m = {}, {}

def solution(arr):
    answer = -1
    nums = [int(i) for i in arr[: : 2]]
    opr = [ j for j in arr[1: : 2]]
    print(nums)
    print(opr)
    for i in range(len(nums)):
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]
    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue
            maxlst , minlst = [] , []
            for k in range(i+1, j + 1):
                if opr[k-1] == '-':
                    mx = M[(i, k-1)] - m[(k, j)]
                    mn = m[(i, k-1)] - M[(k,j)]
                    maxlst.append(mx)
                    minlst.append(mn)
                else:
                    mx = M[(i, k-1)] + M[(k, j)]
                    mn = m[(i, k-1)] + m[(k, j)]
                    maxlst.append(mx)
                    minlst.append(mn)
            M[(i,j)] = max(maxlst)
            m[(i, j)] = min(minlst)
            
    return M[(0, len(nums) - 1)]
   