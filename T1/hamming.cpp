#include <vector>
#include <iostream>
using namespace std;

vector<bool> H;
int n, h;

void printH() {
    for (int i = 0; i < n; ++i) {
        cout << H[i];
    }
    cout << endl;
    return;
}


void hamming(int i, int k) {
    if (k + n - i < h) {
        return;
    }
    if (i == n) {
        printH();
        return;
    }
    hamming(i+1, k);
    if (k < h) {
        H[i] = 1;
        hamming(i+1, k+1);
        H[i] = 0;
    } 
    return;
}


int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n >> h;
        H.resize(n, 0);
        hamming(0, 0);
        if (i + 1 < n) cout << endl;
    }
}
