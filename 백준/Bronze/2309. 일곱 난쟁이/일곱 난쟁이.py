total = [int(input()) for _ in range(9)]
total = sorted(total)
num = sum(total) - 100

found = False
for j in range(9):
    for k in range(j + 1, 9):  # 중복 제거 위해 k = j+1
        if total[j] + total[k] == num:
            fake1 = total[j]
            fake2 = total[k]
            found = True
            break
    if found:
        break

for i in total:
    if i != fake1 and i != fake2:
        print(i)