#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    // 각 삼각형의 행과 열을 계산
    int row_A = int(sqrt(2 * A));
    int col_A = A - row_A * (row_A - 1) / 2;

    int row_B = int(sqrt(2 * B));
    int col_B = B - row_B * (row_B - 1) / 2;

    // 두 삼각형의 행 차이
    int row_diff = abs(row_A - row_B);

    // 같은 행에 있을 경우
    if (row_A == row_B) {
        int col_diff = abs(col_A - col_B);
        cout << col_diff << '\n';
    }
    // 다른 행에 있을 경우
    else {
        // 두 삼각형 간의 가장 짧은 경로의 길이
        int shortest_path = row_diff + min(col_A + row_diff, col_B + row_diff);
        cout << shortest_path << '\n';
    }

    return 0;
}