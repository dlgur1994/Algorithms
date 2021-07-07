#include <iostream>

using namespace std;

int countRule(int num) {
    if (num < 100) {
        return 1;
    }
    else if ((num<1000) && (num%10-num/10%10 == num/10%10-num/100%10)) {
        return 1;
    }
    else {
        return 0;
    }
}

int main(void) {
    int num;
    int cnt = 0;
    cin >> num;

    for (int i=1 ; i<num+1 ; i++) {
        cnt += countRule(i);
    }

    cout << cnt << '\n';
    return 0;
}