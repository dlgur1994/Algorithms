#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    string a, b, lon, sho;
    int temp;

    cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    if (a.length() > b.length()) {
        lon = a;
        sho = b;
    }
    else {
        lon = b;
        sho = a;
    }

    for (int i=0 ; i<sho.length() ; i++) {
        temp = (lon[i]-'0') + (sho[i]-'0');
        if(temp < 10) {
            lon[i] = temp + '0'; 
        }
        else {
            lon[i] = temp - 10 + '0';
            if (i == lon.length()-1) {
                lon.insert(lon.length(), "1");
            }
            else {
                lon[i+1]++;
            }   
        }
    }

    reverse(lon.begin(), lon.end());
    cout << lon << '\n';
    return 0;
}