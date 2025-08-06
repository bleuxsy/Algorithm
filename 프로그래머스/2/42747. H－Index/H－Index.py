def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)
# def solution(citations):
#     answer = 0
#     citations.sort()
#     h = [0] * len(citations)
#     for j in range(len(h)):
#         for i in range(len(citations)):
#             if citations[i] >= j:
#                 h[j] += 1
#     print(h)
#     for i in range(len(h)-1, -1,-1):
#         if i <= h[i]:
#             answer = i
#             return answer