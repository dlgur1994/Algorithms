#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    string a, b;
    int ans[10001] = {0,};

    cin >> a >> b;
    if (b.length() > a.length()) {
        swap(a,b);
    }
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    
    for (int i=0 ; i<a.length() ; i++) {
        if (i < b.length()) {
            ans[i] += a[i]-'0' + b[i]-'0';
        }
        else {
            ans[i] += a[i]-'0';
        }
        if (ans[i] > 9) {
            ans[i] = ans[i]-10;
            ans[i+1]++;
        }
    }

    for (int i=a.length() ; i>-1 ; i--) {
        if (i==a.length() && ans[i]==0) {
            continue;
        }
        cout << ans[i];
    }
    cout << '\n';
    return 0;
}