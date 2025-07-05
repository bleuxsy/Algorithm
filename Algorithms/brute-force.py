from itertools import combinations
 
N,M=map(int,input().split()) 
like=[list(map(int,input().split())) for _ in range(N)] 
result=0
 
for comb in combinations(range(M),3):
    c_sum=0                          
    for r in range(N):                
        p=0
        for idx in comb:
            p=max(p,like[r][idx])     
        c_sum+=p                      
    result=max(result,c_sum)          
print(result)
