"""
세로 길이 H와 가로 길이 W

바닥은 항상 막혀있다고 생각.

물이 고이기 위한 조건
1. 양 사이드에 벽이 있어야 함.

물이 쌓일때는 , 벽을 기준으로 두 벽의 최솟값만큼 차고, 블록의 높이 만큼 뺀 값.

벽을 정하는 기준.
제일 높은 벽 기준으로 작은 값은 무시 큰 값이 생기면 벽으로 정의


1. 벽 찾기
2. 벽 사이에 물이 얼마나 고이는 지 계산.
"""
def find(idx, now):
    global water
    left = 0
    right = 0
    for i in range(idx+1):
        if blocks[i] >= now:
            left = max(left, blocks[i])
    for j in range(idx, W):
        if blocks[j] >= now:
            right = max(right , blocks[j])


    water += min(left, right) - now


    return


H , W = map(int, input().split())
blocks = list(map(int, input().split()))
water = 0



# 본인 왼쪽 중 max , 오른쪽 중 max

for i in range(W):
    find(i, blocks[i])


print(water)