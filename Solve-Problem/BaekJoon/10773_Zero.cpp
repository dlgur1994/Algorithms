#include <iostream>
#include <numeric>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int stack[100000] = {0};
    int num_of_line, temp;
    int top = 0, sum = 0;

    cin >> num_of_line;
    for (int i=0 ; i<num_of_line ; i++) {
        cin >> temp;
        if (temp==0 && top>0) {
            stack[top--] = 0;
        }
        else { stack[top++] = temp; }
    }

    sum = accumulate(stack, stack+top, sum);
    cout << sum << '\n';
    return 0;
}

// #include <stdio.h>
// #include <numeric>

// using namespace std;

// int main(void) {
//     int stack[100000] = {0};
//     int num_of_line, temp;
//     int top = 0, sum = 0;

//     scanf("%d", &num_of_line);
//     for (int i=0 ; i<num_of_line ; i++) {
//         scanf("%d", &temp);
//         if (temp==0 && top>0) {
//             stack[top--] = 0;
//         }
//         else { stack[top++] = temp; }
//     }

//     printf("%d\n", accumulate(stack, stack+top, sum));
//     return 0;
// }