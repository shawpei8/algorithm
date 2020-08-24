#include <iostream>
#include <algorithm>
using namespace std;

struct Birthday {
    int year, month, day;
    Birthday(): year(2000), month(1), day(1) {}
    Birthday(int yr, int mh, int dy) { year = yr, month = mh, day = dy; }
};

struct PerInfo {
    char name[6];
    Birthday d;
};

bool isRational(PerInfo a);
bool cmp(PerInfo a, PerInfo b); // if a < b, return true

int main() {
    int n;
    scanf("%d", &n);
    PerInfo pinfo[n];
    for (int i = 0; i < n; i++) {
        scanf("%s %d/%d/%d", pinfo[i].name, &pinfo[i].d.year, &pinfo[i].d.month, &pinfo[i].d.day);
    }
    sort(pinfo, pinfo+n, cmp);

    int count = 0, old = n-1, young = 0;
    for (int i = 0; i < n; i++) {
        if (isRational(pinfo[i])) {
            if (old > i) old = i;
            if (young < i) young = i;
            count++;
        }
    }
    printf("%d %s %s", count, pinfo[old].name, pinfo[young].name);
    return 0;
}

bool isRational(PerInfo a) {
    PerInfo L = {"", Birthday(1814, 9, 6)};
    PerInfo H = {"", Birthday(2014, 9, 6)};
    if (cmp(a, L) || cmp(H, a)) return false;
    return true;
}

bool cmp(PerInfo a, PerInfo b) {
    if (a.d.year != b.d.year) return a.d.year < b.d.year;
    else if (a.d.month != b.d.month) return a.d.month < b.d.month;
    else return a.d.day < b.d.day;
}