#include <stdio.h>

// Matrix dimensions
#define N 3
#define M 3
#define P 3

// Tile size for matrix multiplication
#define TILE_SIZE 16

// CUDA kernel to perform matrix multiplication
__global__ void matrixMultiply(int *A, int *B, int *C, int n, int m, int p)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int sum = 0;
    if (row < n && col < m)
    {
        for (int k = 0; k < m; k++)
        {
            int a_element = A[row * m + k];
            int b_element = B[k * p + col];
            sum += a_element * b_element;
        }

        C[row * p + col] = sum;
    }
}

int main()
{
    int a[N][M], b[M][P], c[N][P]; // Host matrices
    int *d_a, *d_b, *d_c;          // Device matrices

    // Initialize matrices a and b
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            a[i][j] = i * M + j;
            b[i][j] = i * M + j;
        }
    }

    // Allocate memory on the device
    cudaMalloc((void **)&d_a, N * M * sizeof(int));
    cudaMalloc((void **)&d_b, M * P * sizeof(int));
    cudaMalloc((void **)&d_c, N * P * sizeof(int));

    // Copy data from host to device
    cudaMemcpy(d_a, a, N * M * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, M * P * sizeof(int), cudaMemcpyHostToDevice);

    // Calculate grid and block dimensions based on the tile size
    dim3 dimGrid((P + TILE_SIZE - 1) / TILE_SIZE, (N + TILE_SIZE - 1) / TILE_SIZE);
    dim3 dimBlock(TILE_SIZE, TILE_SIZE);

    // Launch the CUDA kernel
    matrixMultiply<<<dimGrid, dimBlock>>>(d_a, d_b, d_c, N, M, P);

    // Copy the result back to the host
    cudaMemcpy(c, d_c, N * P * sizeof(int), cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // Print the result
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < P; j++)
        {
            printf("%d\t", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}
