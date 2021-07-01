#include <iostream>

using namespace std;

int main(void) {
    int num, fix;
    int sum=0, cnt=0;
    cin >> num;
    fix = num;

    while(true) {
        sum = num/10 + num%10;
        num = (num%10)*10 + sum%10;
        cnt++;
        if (fix==num)
            break;
    }

    cout << cnt << "\n";
    return 0;
}