#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

// Define the size of the vectors
#define N 10

// CUDA kernel to add two vectors
__global__ void vecAdd(float *a, float *b)
{
    // Get the global thread ID
    int id = blockIdx.x * blockDim.x + threadIdx.x;

    // Make sure we do not go out of bounds
    if (id < N)
    {
        b[id] = sinf(a[id]);
    }
}
// Main function
int main()
{
    // Allocate memory for the vectors on the host
    float *h_a = (float *)malloc(N * sizeof(float));
    float *h_b = (float *)malloc(N * sizeof(float));

    // Initialize the vectors
    for (int i = 0; i < N; i++)
    {
        h_a[i] = i;
    }

    // Allocate memory for the vectors on the device
    float *d_a, *d_b;
    cudaMalloc(&d_a, N * sizeof(float));
    cudaMalloc(&d_b, N * sizeof(float));

    // Copy the vectors from the host to the device
    cudaMemcpy(d_a, h_a, N * sizeof(float), cudaMemcpyHostToDevice);

    // Launching the kernel:
    // N Blocks, 1 Thread
    vecAdd<<<N, 1>>>(d_a, d_b);
    // 1 block, N threads
    // vecAdd<<<1, N>>>(d_a, d_b);

    // Copy the result back from the device to the host
    cudaMemcpy(h_b, d_b, N * sizeof(float), cudaMemcpyDeviceToHost);

    // Print the result
    for (int i = 0; i < N; i++)
    {
        printf("%f\n", h_b[i]);
    }

    // Free the memory on the host
    free(h_a);
    free(h_b);

    // Free the memory on the device
    cudaFree(d_a);
    cudaFree(d_b);

    return 0;
}