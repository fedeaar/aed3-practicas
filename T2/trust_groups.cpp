#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> D;
vector<vector<int>> D_T;

int main() {
    while (true) {
        cin >> n >> m;
        if (n+m==0) break;

        map<string,int> name_to_index;
        
        string line; getline(cin, line);
        for (int i=0; i<n; i++) {getline(cin, line); name_to_index[line] = i;}
        
        D.assign(n, vector<int>(0)); D_T.assign(n, vector<int>(0));

        for (int j=0; j<m; j++) {
            string from, to;
            getline(cin, from); getline(cin, to);
            D[name_to_index[from]].push_back(name_to_index[to]);
            D_T[name_to_index[to]].push_back(name_to_index[from]);
        }

        // Completar
    }

    return 0;
}
