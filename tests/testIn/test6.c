#include <stdio.h>
#include <time.h>

int main() {
    long i;
    long total = 0;
    clock_t start_time, end_time;

    start_time = clock();

    for (i = 1; i < 10000000; i++) {
        total += i;
    }

    end_time = clock();

    printf("C: The sum is %ld\n", total);
    printf("C: Time taken = %lf seconds\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);

    return 0;
}
