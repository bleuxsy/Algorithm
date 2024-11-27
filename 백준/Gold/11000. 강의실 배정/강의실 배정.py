import heapq
import sys
input = sys.stdin.readline
heap =[]
N = int(input())
arr=[]
total =0
for i in range(N):
  s,t = map(int,input().split())
  arr.append((s,t))
arr.sort(key = lambda x: x[0])
heapq.heappush(heap, arr[0][1])
for i in range(1,N):
  if heap[0] > arr[i][0]:
    heapq.heappush(heap, arr[i][1])
  else:
    heapq.heappop(heap)
    heapq.heappush(heap,arr[i][1])
print(len(heap))
    
