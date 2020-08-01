#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int sum(vector<int> arr) {
    int result = 0;
    for (auto i : arr)
        result += i;
    return result;
}

char gestrue(vector<int> arr) {
    vector<int> tmp(arr.begin(), arr.end());
    sort(tmp.begin(), tmp.end());
    if (tmp[2] == arr[2]) return 'B';
    if (tmp[2] == arr[0]) return 'C';
    if (tmp[2] == arr[1]) return 'J';
}

int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    int ties = 0;
    vector<int> awin(3, 0);
    vector<int> bwin(3, 0);

    char a, b;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        switch (a)
        {
        case 'C':
            if (b == 'J') awin[0]++;
            if (b == 'B') bwin[2]++;
            if (b == 'C') ties++;
            break;
        case 'J':
            if (b == 'B') awin[1]++;
            if (b == 'C') bwin[0]++;
            if (b == 'J') ties++;
            break;
        case 'B':
            if (b == 'C') awin[2]++;
            if (b == 'J') bwin[1]++;
            if (b == 'B') ties++;
            break;
        default:
            break;
        }
    }
    int awins = sum(awin);
    int bwins = sum(bwin);
    cout << awins << ' ' << ties << ' ' << bwins << endl;
    cout << bwins << ' ' << ties << ' ' << awins << endl;
    cout << gestrue(awin) << ' ' << gestrue(bwin) << endl;
    return 0;
}