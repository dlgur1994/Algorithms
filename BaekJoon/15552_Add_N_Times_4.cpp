#include <iostream>

using namespace std;

int main(void) {
    cin.tie(NULL); // stop flushing the stream
    ios::sync_with_stdio(false); // it asynchronizes the input and output of C and C++

    int n, a, b;
    cin >> n;

    for (int i=0 ; i<n ; i++) {
        cin >> a >> b;
        cout << a+b << "\n";
    }

    return 0;
}