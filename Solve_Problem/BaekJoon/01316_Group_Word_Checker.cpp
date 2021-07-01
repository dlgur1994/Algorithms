#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int N;
    int cnt = 0;

    cin >> N;
    
    for (int i=0 ; i<N ; i++) {
        int checker[26] = {0,};
        string word;
        char cur = 'A';
        cin >> word;
        for (int j=0 ; j<word.length() ; j++) {
            if (j == word.length()-1) {
                if (word[j]==cur || checker[word[j]-97] == 0) {
                    cnt++;
                }
            }
            else if (word[j] == cur) {
                continue;
            }
            else if (checker[word[j]-97] == 0) {
                checker[word[j]-97]++;
                cur = word[j];
            }
            else {
                break;
            }
        }
    }

    cout << cnt << '\n';
    return 0;
}