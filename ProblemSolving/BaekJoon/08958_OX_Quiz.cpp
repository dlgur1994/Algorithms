#include <iostream>

using namespace std;

int main(void) {
    int n, idx, cnt, sum;
    string str;
    cin >> n;

    for (int i=0 ; i<n ; i++) {
        cin >> str;
        idx = 0;
        cnt = 1;
        sum = 0;
        while(str[idx] != '\0') {
            if (str[idx] == 'O') {
                sum += cnt;
                cnt++;
            }
            else {
                cnt = 1;
            }
            idx++;
        }
        cout << sum << '\n';
    }

    return 0;
}