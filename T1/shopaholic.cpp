#include <iostream>
#include <vector>
using namespace std;

void counting_sort(vector<int> &v, vector<int> &count) {
    int iterador = 0;
    for (int j = 0; j < 20000; j++) {
        while (count[j] > 0) {
            v[iterador] = j;
            count[j] --;
            iterador++;
        }
    }
}

int maximo_descuento(vector<int> &v) {
    int i = v.size() - 3;
    int descuento = 0;
    while (i >= 0) {
        descuento += v[i];
        i -= 3;
    }
    return descuento;
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int n; cin >> n;
        vector<int> v(n);
        vector<int> count(20000);
        for (int j = 0; j < n; j++) {
            int valor; cin >> valor;
            count[valor]++;
        }
        counting_sort(v,count);
        cout << maximo_descuento(v) << "\n";
    }
}