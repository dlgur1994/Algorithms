#include <iostream>

using namespace std;

int main(void) {
    string str;
    int idx = 0;
    int chs[26];
    fill_n(chs, 26, -1);
    
    cin >> str;

    while (str[idx] != '\0') {
        if (chs[str[idx]-97] == -1) {
            chs[str[idx]-97] = idx;
        }
        idx++;
    }

    for (int i=0 ; i<26 ; i++) {
        if (i == 25) {
            cout << chs[i] << '\n';
            break;
        }
        cout << chs[i] << ' ';
    }
    return 0;
}