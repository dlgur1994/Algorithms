#include <iostream>

using namespace std;

int main(void) {
    int A,B,C, mul;
    int cnts[10] = {0,};
    cin >> A >> B >> C;

    mul = A*B*C;
    while(mul>0) {
        cnts[mul%10]++;
        mul /= 10;
    }
    
    for (int i=0 ; i<10 ; i++) {
        cout << cnts[i] << "\n";
    } 
    return 0;
}