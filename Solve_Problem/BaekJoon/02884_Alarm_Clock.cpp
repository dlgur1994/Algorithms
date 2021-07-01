#include <iostream>

using namespace std;

int main(void) {
    int hr, min;
    cin >> hr >> min;

    // Subtract 45 minutes from min
    min -= 45;

    // if min is less than zero, borrow an hour and convert it to 60 minutes
    if (min < 0) {
        min += 60;
        hr -= 1;

        // if hr becomes less than zero, change it to 23
        if (hr < 0)
        hr = 23;
    }
    
    cout << hr << " " << min << "\n";
    return 0;
}