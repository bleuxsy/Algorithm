import sys
from collections import deque


N = int(sys.stdin.readline())
mydeq = deque()


for _ in range(N):
    
    command = list(map(int,sys.stdin.readline().split()))
    
    
    S = int(command[0])
    
    if S == 1:
        
        X = int(command[1])
        mydeq.append(X)
    elif S == 2:
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq.pop())
        
    elif S == 3:
       print(len(mydeq))
    elif S == 4:
        if len(mydeq) == 0:
            print(1)
        else:
            print(0)
        
    elif S == 5:
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq[-1])
   