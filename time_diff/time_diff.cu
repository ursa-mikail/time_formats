#include <stdio.h>
#include <cuda_runtime.h>

__global__ void dummy_kernel() {
    // Just wait a little on GPU
    for (int i = 0; i < 100000000; ++i);
}

int main() {
    cudaEvent_t start, end;
    float elapsed_ms;

    cudaEventCreate(&start);
    cudaEventCreate(&end);

    cudaEventRecord(start, 0);
    dummy_kernel<<<1, 1>>>();
    cudaEventRecord(end, 0);
    cudaEventSynchronize(end);

    cudaEventElapsedTime(&elapsed_ms, start, end);

    int sec = (int)(elapsed_ms / 1000);
    int ms = ((int)elapsed_ms) % 1000;
    int us = (int)((elapsed_ms - (int)elapsed_ms) * 1000);
    int ns = (int)((elapsed_ms * 1000000)) % 100;

    printf("Delta: 0000-00-00_0000_%02d_%03d_%03d_%02d\n", sec, ms, us, ns);
    printf("Delta (seconds): %.9f\n", elapsed_ms / 1000.0);

    cudaEventDestroy(start);
    cudaEventDestroy(end);

    return 0;
}

