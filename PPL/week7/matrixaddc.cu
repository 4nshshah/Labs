#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>

#define SIZE 3

__global__ void matrixAddition(int *A, int *B, int *C, int width)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < width && col < width)
    {
        C[row * width + col] = A[row * width + col] + B[row * width + col];
    }
}

int main()
{
    int *h_A, *h_B, *h_C;
    int *d_A, *d_B, *d_C;

    // Allocate memory for matrices A, B, and C
    int matrixSize = SIZE * SIZE * sizeof(int);
    h_A = (int *)malloc(matrixSize);
    h_B = (int *)malloc(matrixSize);
    h_C = (int *)malloc(matrixSize);

    // Initialize matrices A and B
    for (int i = 0; i < SIZE * SIZE; i++)
    {
        h_A[i] = i;
        h_B[i] = i;
    }

    // Allocate memory in GPU
    cudaMalloc((void **)&d_A, matrixSize);
    cudaMalloc((void **)&d_B, matrixSize);
    cudaMalloc((void **)&d_C, matrixSize);

    // Copy matrices A and B to GPU
    cudaMemcpy(d_A, h_A, matrixSize, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, matrixSize, cudaMemcpyHostToDevice);

    // Set up grid and block dimensions
    dim3 dimBlock(16, 16);
    dim3 dimGrid((SIZE + dimBlock.x - 1) / dimBlock.x, (SIZE + dimBlock.y - 1) / dimBlock.y);

    // Launch kernel
    matrixAddition<<<dimGrid, dimBlock>>>(d_A, d_B, d_C, SIZE);

    // Copy result matrix C from GPU
    cudaMemcpy(h_C, d_C, matrixSize, cudaMemcpyDeviceToHost);

    // Print result matrix C
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            printf("%d ", h_C[i * SIZE + j]);
        }
        printf("\n");
    }

    // Free memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    free(h_A);
    free(h_B);
    free(h_C);

    return 0;
}