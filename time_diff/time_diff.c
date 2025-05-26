#include <stdio.h>
#include <time.h>

void format_and_print_diff(struct timespec start, struct timespec end) {
    time_t delta_sec = end.tv_sec - start.tv_sec;
    long delta_nsec = end.tv_nsec - start.tv_nsec;

    if (delta_nsec < 0) {
        delta_sec -= 1;
        delta_nsec += 1000000000L;
    }

    // Extract ms, us, ns
    int ms = delta_nsec / 1000000;
    int us = (delta_nsec / 1000) % 1000;
    int ns = delta_nsec % 100;

    printf("Delta: 0000-00-00_0000_%02ld_%03d_%03d_%02d\n", delta_sec, ms, us, ns);
    printf("Delta (seconds.nanoseconds): %ld.%09ld\n", delta_sec, delta_nsec);
}

int main() {
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    sleep(5);  // Simulate work or delay
    clock_gettime(CLOCK_MONOTONIC, &end);

    format_and_print_diff(start, end);

    return 0;
}

