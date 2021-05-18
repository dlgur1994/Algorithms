#include <iostream>

using namespace std;

bool flags[10001] = {false, };

void countNum(int num) {
    int temp = 0;
    int cpy = num;
    while (cpy > 0) {
        temp += cpy%10;
        cpy /= 10;
    }
    flags[num+temp] = true; 
}

int main(void) {
    for (int i=0 ; i<10001 ; i++) {
        countNum(i);
    }

    for (int i=1 ; i<10001 ; i++) {
        if (flags[i]==false) {
            cout << i << '\n';
        }
    } 
    
    return 0;
}