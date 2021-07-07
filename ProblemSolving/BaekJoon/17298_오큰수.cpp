#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int size_of_arr;
    cin >> size_of_arr;

    int values[size_of_arr], result[size_of_arr];
    int cur_max, cnt;

    for (int i=0 ; i<size_of_arr ; i++) {
        cin >> values[i];
        cur_max = values[i];
        
        if (values[i] > cur_max) {
            for (int j=cnt ; j<i ; j++) {
                result[j] = cur_max;
            }
            cnt = 0;
        }
        cnt++;
    }

    for (int i=0 ; i<size_of_arr ; i++) {
        cout << result[i] << ' ';
    }
    cout << '\n';
    return 0;
}