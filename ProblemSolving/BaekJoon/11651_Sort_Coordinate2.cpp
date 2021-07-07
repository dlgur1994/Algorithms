#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int num_of_points, x, y;
    vector<pair<int,int> > points;

    scanf("%d", &num_of_points);
    for (int i=0 ; i<num_of_points ; i++) {
        scanf("%d %d", &x, &y);
        points.push_back(pair<int,int>(y,x));
    }

    sort(points.begin(), points.end());

    for (int i=0 ; i<num_of_points ; i++) {
        printf("%d %d\n", points[i].second, points[i].first);
    }
    return 0;
}