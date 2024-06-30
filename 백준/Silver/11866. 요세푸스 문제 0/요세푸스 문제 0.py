import sys
N , K = map(int,sys.stdin.readline().split())
queue = [ i for i in range(1, N+1)]
d = 0
result = []
while queue:
  d += (K-1)
  if d >= len(queue):
    d %= len(queue)
  result.append(str(queue.pop(d)))
print("<",", ".join(result),">" ,sep="")
