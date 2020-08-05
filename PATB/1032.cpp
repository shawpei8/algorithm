#include <vector>
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> s(n+1);
    int sno, score;
    for (int i = 0; i < n; i++) {
        cin >> sno >> score;
        s[sno] += score;
    }
    int no = 1, max = s[1];
    for (int i = 0; i < n; i++) {
        if (max < s[i]) {
            max = s[i];
            no = i;
        }
    }
    cout << no << ' ' << max;
    return 0;
}