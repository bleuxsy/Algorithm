a = input()
b = input()
LCS = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for j in range(1, len(a)+1):
    for i in range(1, len(b)+1):
        if a[j-1] == b[i-1]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])


print(max(max(LCS)))