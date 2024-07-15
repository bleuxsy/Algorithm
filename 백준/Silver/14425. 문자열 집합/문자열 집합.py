#14425번
N , M = map(int,input().split())
S = set()
result = 0
for _ in range(N):
  data = input().strip()
  S.add(data)
for i in range(M):
  data = input().strip()
  if data in S:
    result += 1
print(result)
#strip :문자열의 양 끝에 있는 불필요한 공백 제거
#split :문자열을 특정 구분자를 기준으로 나누어 리스트로 반환