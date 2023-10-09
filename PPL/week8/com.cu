#include <stdio.h>

// Define matrix dimensions (M and N)
#define M 4
#define N 4

// Kernel to perform the 1's complement operation on non-border elements
__global__ void onesComplement(int *A, int *B, int rows, int cols)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row >= 0 && row < rows && col >= 0 && col < cols)
    {
        // Check if the current element is a non-border element
        if (row > 0 && row < rows - 1 && col > 0 && col < cols - 1)
        {
            // Calculate the index for the current element
            int index = row * cols + col;
            // Calculate the 1's complement of the element and store it in B
            int number = A[index];
            int ulta = 0;
            for (int i = 0; number > 0; i++)
            {
                ulta *= 10;
                ulta += 1 - number % 2;
                number = number / 2;
            }
            B[index] = ulta;
        }
        else
        {
            // Copy border elements as-is
            B[row * cols + col] = A[row * cols + col];
        }
    }
}

int main()
{
    int A[M][N]; // Input matrix A
    int B[M][N]; // Output matrix B

    // Initialize matrix A with example values
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = i * N + j;
        }
    }

    int *d_A, *d_B; // Device pointers for matrices A and B

    // Allocate memory on the GPU for matrices A and B
    cudaMalloc((void **)&d_A, M * N * sizeof(int));
    cudaMalloc((void **)&d_B, M * N * sizeof(int));

    // Copy matrix A from host to device
    cudaMemcpy(d_A, A, M * N * sizeof(int), cudaMemcpyHostToDevice);

    // Define thread and block dimensions
    dim3 threadsPerBlock(16, 16);
    dim3 numBlocks((N + threadsPerBlock.x - 1) / threadsPerBlock.x, (M + threadsPerBlock.y - 1) / threadsPerBlock.y);

    // Launch the CUDA kernel
    onesComplement<<<numBlocks, threadsPerBlock>>>(d_A, d_B, M, N);

    // Copy matrix B from device to host
    cudaMemcpy(B, d_B, M * N * sizeof(int), cudaMemcpyDeviceToHost);

    // Free GPU memory
    cudaFree(d_A);
    cudaFree(d_B);

    // Print matrix B (1's complement of non-border elements) in binary
    printf("Matrix B (1's complement of non-border elements in binary):\n");
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }

    return 0;
}
