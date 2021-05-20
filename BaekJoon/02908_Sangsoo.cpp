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

// #include <iostream>

// using namespace std;

// int main(void) {
//     int num1, num2, cp1, cp2, big;
//     int result = 0;
//     cin >> num1 >> num2;
//     cp1 = num1;
//     cp2 = num2;

//     for (int i=0 ; i<3 ; i++) {
//         if (cp1%10 > cp2%10) {
//             big = num1;
//             break;
//         }
//         else if (cp1%10 < cp2%10) {
//             big = num2;
//             break;
//         }
//         else {
//             cp1 /= 10;
//             cp2 /= 10;
//         }
//     }

//     for (int i=0 ; i<3 ; i++) {
//         result *= 10;
//         result += big%10;
//         big /= 10; 
//     }

//     cout << result << '\n';
//     return 0;
// }