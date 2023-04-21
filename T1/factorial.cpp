#include <vector>
#include <iostream>

using namespace std;


typedef long long ll;

vector<ll> factoriales = {1, 2, 6, 24, 120, 720, 5040, 40320};
vector<ll> C;


ll factorial(int n) {
    int k = 7;
    int i = 0;
    while (n > 0) {
        int v = n / factoriales[k];
        if (v > 0) {
            i += v;
            n = n - v * factoriales[k];
        } else {
            k--;
        }
    }
    return i;
}

int main() {
    int n, t; 
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        C.resize(n);
        ll res = factorial(n);
        cout << res << endl;
    }
}
