def back(idx, res):
    global maxx, minn

    if idx == N:
        maxx = max(maxx, res)
        minn = min(minn, res)
        return

    # +
    if cmd[0] > 0:
        cmd[0] -= 1
        back(idx + 1, res + A[idx])
        cmd[0] += 1

    # -
    if cmd[1] > 0:
        cmd[1] -= 1
        back(idx + 1, res - A[idx])
        cmd[1] += 1

    # *
    if cmd[2] > 0:
        cmd[2] -= 1
        back(idx + 1, res * A[idx])
        cmd[2] += 1

    # /
    if cmd[3] > 0:
        cmd[3] -= 1
        if res < 0:
            back(idx + 1, - (abs(res) // A[idx]))
        else:
            back(idx + 1, res // A[idx])
        cmd[3] += 1


N = int(input())
A = list(map(int, input().split()))
cmd = list(map(int, input().split()))

maxx = -10**18
minn =  10**18

back(1, A[0])  # idx=1부터 시작 (A[0]은 이미 res에 들어감)

print(maxx)
print(minn)