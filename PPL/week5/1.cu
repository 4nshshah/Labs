#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
__global__ void add(int *a, int *b, int *c)
{
    int i = threadIdx.x + (blockIdx.x * blockDim.x);
    c[i] = a[i] + b[i];
}

int main(void)
{
    int a[4] = {1, 2, 3, 4}, b[4] = {1, 2, 3, 4}, c[4];
    // host copies of variables a, b & c
    int *d_a = (int *)malloc(4 * sizeof(int));
    int *d_b = (int *)malloc(4 * sizeof(int));
    int *d_c = (int *)malloc(4 * sizeof(int));
    // device copies of variables a, b & c
    int size = sizeof(a) / sizeof(int);
    // Allocate space for device copies of a, b, c
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);
    // Setup input values
    // Copy inputs to device
    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
    // Launch add() kernel on GPU
    add<<<4, 1>>>(d_a, d_b, d_c);
    // Copy result back to host
    cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);
    for (int i = 0; i < 4; i++)
        printf("Result: % d\n", c[i]);
    // Cleanup
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}