#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // 加快输入
    int n, p;
    cin >> n >> p;
    long a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, a + n); // 预排序

    int count = 1;
    int i = 0, j = 1;
    while (j < n) {
        a[j] <= a[i] * p ? count++ : i++;
        j++;
    }
    cout << count;
    return 0;
}