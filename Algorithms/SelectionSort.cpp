#include <stdio.h>

int main(void) {
    int arr[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
    int min, id, temp;

    for (int i=0 ; i<9 ; i++) {
        min = 11;
        for (int j=i ; j<10 ; j++) {
            if (arr[j] < min) {
                min = arr[j];
                id = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[id];
        arr[id] = temp;
    }

    for (int i=0 ; i<10 ; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}