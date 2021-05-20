#include <iostream>

using namespace std;

int main(void) {
    int num1, num2;
    int rev1=0, rev2=0;
    cin >> num1 >> num2;

    for (int i=0 ; i<3 ; i++) {
        rev1 *= 10;
        rev2 *= 10;
        rev1 += num1%10;
        rev2 += num2%10;
        num1 /= 10;
        num2 /= 10;
    }

    if (rev1 > rev2) {
        cout << rev1 << '\n';
    }
    else {
        cout << rev2 << '\n';
    }
    return 0;
}