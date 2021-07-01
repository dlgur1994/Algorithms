#include <stdio.h>

int fib(int num) {
    if (num<2) return num;
    return (fib(num-1)+fib(num-2));
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", fib(n));
    return 0;
}