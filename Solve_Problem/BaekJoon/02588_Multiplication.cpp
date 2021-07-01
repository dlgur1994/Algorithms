#include <iostream>

using namespace std;

int main(void) {
    int a, b, mult;
    cin >> a >> b;
    mult = a*b;

    for (int i=0 ; i<3 ; i++) {
        cout << a*(b%10) << "\n";
        b /= 10;
    }
    cout << mult << "\n";
    return 0;
}