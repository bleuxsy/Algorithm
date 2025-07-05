import sys
N , M = map(int,input().split())
knowList = set(input().split()[1:])
parties = []
for i in range(M):
  parties.append(set(input().split()[1:]))
for j in range(M):
  for party in parties:
    if party.intersection(knowList):
      knowList = knowList.union(party)
cnt = 0
for party in parties:
  if party & knowList:
    continue
  cnt+=1
print(cnt)