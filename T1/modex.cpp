#include <iostream>

using namespace std;

// Completar
int mod_bin_exp(int x, int y, int n) {
    if (y == 0) return 1;
    int modexp = mod_bin_exp(x,y/2,n);
    if (y % 2 == 0) return (modexp*modexp) % n;
    else return (((modexp*modexp) % n) * x) % n;

}

int main() {
    int c; cin >> c;

    while (c--) {
        int x, y, n; cin >> x >> y >> n;
        cout << mod_bin_exp(x, y, n) << endl;
    }

    return 0;
}
