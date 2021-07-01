#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void) {
    int num_of_points, x, y;
    pair<int,int> points[100000];

    scanf("%d", &num_of_points);
    for (int i=0 ; i<num_of_points ; i++) {
        scanf("%d %d", &x, &y);
        points[i] = pair<int,int>(x,y);
    }

    sort(points, points+num_of_points);

    for (int i=0 ; i<num_of_points ; i++) {
        printf("%d %d\n", points[i].first, points[i].second);
    }
    return 0;
}