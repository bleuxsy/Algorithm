import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    temps = list(map(int, input().split()))

    # 첫 K일 합으로 초기화
    window_sum = sum(temps[:K])
    best = window_sum

    # 한 칸씩 밀면서: 들어오는 값 더하고, 나가는 값 빼기
    for i in range(K, N):
        window_sum += temps[i] - temps[i - K]
        if window_sum > best:
            best = window_sum

    print(best)

if __name__ == "__main__":
    main()