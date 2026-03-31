import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1

best = float('inf')
answer = (0, 0)

while left < right:
    s = arr[left] + arr[right]

    if abs(s) < best:
        best = abs(s)
        answer = (arr[left], arr[right])

    if s > 0:
        right -= 1
    else:
        left += 1

print(answer[0], answer[1])