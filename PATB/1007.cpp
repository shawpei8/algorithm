#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    bool marks[n+1] = {false};
    
    int count = 0;
    for (int i = 0; i < n+1; i++) {
        if (isPrime(i)) {
            marks[i] = true;
            if (i - 2 >= 0 && marks[i-2])
                count++;
        } 
    }
    cout << count << endl;
    return 0;
}