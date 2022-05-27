#include <iostream>
#include <cassert>
using namespace std;

int calcSum(int m, int n) {
    int ascMatrix[m][n];
    int descMatrix[n][m];

    // constructing the matrixes
    for (int i = 1; i <= m * n; i++) {
        ascMatrix[(i - 1) / n][(i - 1) % n] = i;
        descMatrix[(i - 1) / m][(i - 1) % m] = (m * n) - i + 1;
    }

    int total = 0;

    // matrix multiplication
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < n; k++) {
                total += ascMatrix[i][k] * descMatrix[k][j];
            }
        }
    }
    return total;
}

int main() {
    cout << "Testing (2, 3)" << endl;
    assert (calcSum(2, 3) == 131);
    cout << "(2, 3) passed" << endl;
    cout << "Testing (3, 3)" << endl;
    assert (calcSum(3, 3) == 621);
    cout << "(3, 3) passed" << endl;
}