T = int(input())
for _ in range(T):
  H,W,N = map(int,input().split())
  ho = (N//H )+ 1
  Floor = N%H
  if(Floor == 0) :
     Floor = H
     ho -= 1
  print(Floor*100+ho)
  