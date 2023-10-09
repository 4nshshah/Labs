#include <stdio.h>
#include <cuda.h>
// Kernel function to replace each row of the matrix with the corresponding powers of its elements
__global__ void replace_rows_kernel(float *matrix, int m, int n)
{
    int row = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < m)
    {
        for (int j = 0; j < n; j++)
        {
            int index = row * n + j;
            matrix[index] = powf(matrix[index], row + 1);
        }
    }
}

int main()
{
    // Matrix dimensions
    int m = 3;
    int n = 3;

    // Matrix A
    float matrix[m][n];

    // Read matrix A from the user
    printf("Enter the elements of the matrix A:\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%f", &matrix[i][j]);
        }
    }

    // Allocate memory on device
    float *d_matrix;
    cudaMalloc((void **)&d_matrix, m * n * sizeof(float));

    // Copy matrix A from host to device
    cudaMemcpy(d_matrix, matrix, m * n * sizeof(float), cudaMemcpyHostToDevice);

    // Define grid and block dimensions
    int block_size = 256;
    int grid_size = (m + block_size - 1) / block_size;

    // Launch kernel
    replace_rows_kernel<<<grid_size, block_size>>>(d_matrix, m, n);

    // Copy matrix A from device to host
    cudaMemcpy(matrix, d_matrix, m * n * sizeof(float), cudaMemcpyDeviceToHost);

    // Print the modified matrix A
    printf("Modified matrix A:\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%.2f ", matrix[i][j]);
        }
        printf("\n");
    }

    // Free memory on device
    cudaFree(d_matrix);

    return 0;
}