#include <iostream>
#include <vector>
using namespace std;

int mayorMonto(vector<vector<int>> &M, int i, int c, vector<int> &p, vector<int>& w) {
    if (i == p.size() || c == 0) return 0;
    if (M[c][i] == -1) {
        int maxVal = mayorMonto(M,i+1,c, p, w);
        if (c - w[i] >= 0) {
            maxVal = max(maxVal, p[i] + mayorMonto(M, i+1, c - w[i], p , w));
        }
        M[c][i] = maxVal;
    }
    return M[c][i];
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int montoMax = 0;
        int n; cin >> n;
        vector<int> p(n);
        vector<int> w(n);
        for (int j = 0; j < n; j++) {
            cin >> p[j];
            cin >> w[j];
        }
        int g; cin >> g;
        vector<int> c(g);
        vector<vector<int>> M(31, vector<int>(n,-1));
        for (int j = 0; j < g; j++) {
            cin >> c[j];
            montoMax += mayorMonto(M, 0, c[j], p, w);
        }
        cout << montoMax << endl;
    }
    return 0;
}
