#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 100001;

int main() {
    int start, N, K, tmp;
    cin >> start >> N >> K;

    int data[MAX], next[MAX], List[MAX]; 
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        cin >> data[tmp] >> next[tmp];
    }

    int cnt = 0; // 实际链表长度
    while (start != -1) {
        List[cnt++] = start;
        start = next[start];
    }

    for (int i = 0; i < (cnt - cnt % K); i += K) {
        reverse(List + i, List + i + K);
    }

    for (int i = 0; i < cnt - 1; i++) {
        printf("%05d %d %05d\n", List[i], data[List[i]], List[i + 1]);
    }
    printf("%05d %d -1", List[cnt - 1], data[List[cnt - 1]]);
    return 0;
}