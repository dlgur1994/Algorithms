#include <iostream>

using namespace std;

int main(void) {
    int temp;
    int cnt = 0; 
    int nums[42] = {0,};
    for (int i=0 ; i<10 ; i++) {
        cin >> temp;
        nums[temp%42] = 1;
    }

    for (int i=0 ; i<42 ; i++) {
        if (nums[i] == 1) {
            cnt++;
        }
    }

    cout << cnt << "\n";
    return 0;
}