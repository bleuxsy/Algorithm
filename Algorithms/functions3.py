#문제 05
def soultions(arr1,arr2):
    r1 , c1 = len(arr1) , len(arr1[0])
    r2 , c2 = len(arr2), len(arr2[0])
    result = [[0]* c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result 

#문제 06
def solutions2(N, stages):
    challenger = [0]* (N+2)
    for stage in stages:
        challenger[stage] += 1
    total = len(stages)
    fails = {}
    for i in range(1,N+1):
        if challenger[i] == 0:
            fails[i] = challenger[i]/total
            total -= challenger[i]
    result = sorted(fails, key = lambda x : fails[x], reverse= True)
    return result

