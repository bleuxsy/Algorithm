# def f(A):
#     total =0
#     for i in range(1,A+1):
#         if A % i == 0:
#             total += i
#     return total
# def g(x):
#     result = 0
#     for i in range(1,x+1):
#         result += f(i)
#     return result
# N = int(input())
# print(g(N))
N= int(input())
total =0
for i in range(1, N+1):
    total += (N//i)*i
print(total)