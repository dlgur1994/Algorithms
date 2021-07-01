#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
    int fixed;
    int vari;
    int price;
    int point;

    cin >> fixed >> vari >> price;
    // if 'price' is equal to or less than 'vari', there is no break-even point
    if (price==vari || price<vari) {
        cout << -1 << '\n';
        return 0;
    }

    point = fixed/(price-vari);
    // it is when revenue and expenditure are at the same point
    if (point == ceil(point)) {
        point++;
    }
    else {
        point = ceil(point);
    }
    cout << point << '\n';
    return 0;
}