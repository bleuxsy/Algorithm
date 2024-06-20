N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
sum_t = 0
for size in sizes:
    sum_t += (size // T) + (1 if size % T > 0 else 0)
max_pen_bundles = N // P
remaining_pens = N % P
print(sum_t)
print(max_pen_bundles)
print(remaining_pens)

