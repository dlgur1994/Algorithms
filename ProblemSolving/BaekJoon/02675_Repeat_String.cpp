#include <iostream>

using namespace std;

int main(void) {
    int N;
    cin >> N;
    int num;
    string str;
    string result;
    
    for (int i=0 ; i<N ; i++) {
        cin >> num >> str;
        result = "";
        for (int j=0 ; j<str.length() ; j++) {
            for (int k=0 ; k<num ; k++) {
                result += str[j];
            }
        }
        cout << result << '\n';
    }

    return 0;
}