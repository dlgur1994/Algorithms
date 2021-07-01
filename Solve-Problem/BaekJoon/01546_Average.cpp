#include <iostream>

using namespace std;

int main(void) {
    int N;
    int max = 0;
    double sum = 0;
    cin >> N;
    int scores[N];
    for (int i=0 ; i<N ; i++) {
        cin >> scores[i];
        if (scores[i] > max)
            max = scores[i];
    }

    for (int i=0 ; i<N ; i++) {
        sum += double(scores[i])/max*100;
    }

    cout << sum/double(N) << "\n";
    return 0;
}