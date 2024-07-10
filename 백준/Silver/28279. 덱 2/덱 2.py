import sys
from collections import deque


N = int(sys.stdin.readline())
mydeq = deque()


for _ in range(N):
    
    command = list(map(int,sys.stdin.readline().split()))
    
    
    S = int(command[0])
    
    if S == 1:
        
        X = int(command[1])
        mydeq.appendleft(X)
    elif S == 2:
        
        X = int(command[1])
        mydeq.append(X)
    elif S == 3:
        
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq.popleft())
    elif S == 4:
        
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq.pop())
    elif S == 5:
        
        print(len(mydeq))
    elif S == 6:
       
        if len(mydeq) == 0:
            print(1)
        else:
            print(0)
    elif S == 7:
        
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq[0])
    elif S == 8:
        
        if len(mydeq) == 0:
            print(-1)
        else:
            print(mydeq[-1])
