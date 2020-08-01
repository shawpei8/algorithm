#include <iostream>
#include <algorithm>
using namespace std;

struct Student {
    int id, de, cai;
    int total;
    int level = 5; // 5个等级，1为最优
};

bool cmp(Student a, Student b) {
    if (a.level != b.level) return a.level < b.level;
    else if (a.total != b.total) return a.total > b.total;
    else if (a.de != b.de) return a.de > b.de;
    else return a.id > b.id;
}

int main() {
    ios::sync_with_stdio(false);
    int N, L, H, M = 0;
    cin >> N >> L >> H;
    Student studs[N];
    int id, de, cai;
    for (int i = 0; i < N; i++) {
        cin >> id >> de >> cai;
        studs[i].id = id;
        studs[i].de = de;
        studs[i].cai = cai;
        studs[i].total = de + cai;
        if (de >= H && cai >= H) {
            studs[i].level = 1;
        }else if (de >= H && cai >= L) {
            studs[i].level = 2;
        }else if (de >= L && cai >= L && de >= cai) {
            studs[i].level = 3;
        }else if (de >= L && cai >= L) {
            studs[i].level = 4;
        }else {
            M++;
        }
    }
    // 排序
    sort(studs, studs+N, cmp);

    // 输出
    M = N - M;
    cout << M << endl;
    for (int i = 0; i < M; i++) {
        cout << studs[i].id << ' ' << studs[i].de << ' ' << studs[i].cai << endl;
    }

    return 0;
}