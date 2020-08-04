#include <iostream>
using namespace std;

const int MAX = 100000;

struct Node {
    int data, next;
} List[MAX];

int reverseList(int start, int len, int k);

int main() {
    int start, N, K; 
    cin >> start >> N >> K;

    int addr, data, next;
    for (int i = 0; i < N; i++) {
        cin >> addr >> data >> next;
        List[addr].data = data;
        List[addr].next = next;
    }

    int m = 0; // 实际链表长度
    for (int i = start; i != -1; i = List[i].next) {
        m++;
    }

    int newStart = reverseList(start, m, K);
    for (int i = newStart; i != -1; i = List[i].next) {
        cout << i << ' ' << List[i].data << ' ' << List[i].next << endl;
    }
    return 0;
}

int reverseList(int start, int len, int k) {
    int n = len / k;
    int head, tail;
    for (int i = 0; i < n; i++) {
        
    }
}