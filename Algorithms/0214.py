import sys
sys.stdin = open("in1.txt", "r")
res =''
if __name__ == "__main__":
    N , M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst)
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == M:
            print(mid+1)
            break
        if lst[mid] < M:
            start = mid+1
        else:
            end = mid-1
