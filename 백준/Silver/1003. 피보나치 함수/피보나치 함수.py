import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        zero, one = 1, 0  # n=0
        z1, o1 = 0, 1     # n=1
        for _ in range(2, n + 1):
            zero, one, z1, o1 = z1, o1, zero + z1, one + o1
        print(z1, o1)