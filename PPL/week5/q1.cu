#include <stdio.h>
#include <cuda.h>
#include <stdlib.h>

#define N 105

__global__ void vecAdd(int *a, int *b, int *c)
{
    int i = threadIdx.x + blockDim.x * blockIdx.x;
    if (i < N)
    {
        c[i] = a[i] + b[i];
    }
}

int main()
{
    int *a = (int *)malloc(N * sizeof(int));
    int *b = (int *)malloc(N * sizeof(int));
    int *c = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
    {
        a[i] = i;
        b[i] = i;
    }

    int *da, *db, *dc;
    cudaMalloc(&da, sizeof(a));
    cudaMalloc(&db, sizeof(b));
    cudaMalloc(&dc, sizeof(c));

    cudaMemcpy(da, a, sizeof(a), cudaMemcpyHostToDevice);
    cudaMemcpy(db, b, sizeof(b), cudaMemcpyHostToDevice);
    cudaMemcpy(dc, c, sizeof(c), cudaMemcpyHostToDevice);

    vecAdd<<<N, 1>>>(da, db, dc);

    cudaMemcpy(c, dc, sizeof(c), cudaMemcpyDeviceToHost);
    for (int i = 0; i < N; i++)
        printf("%d\n", c[i]);

    // free(a);
    // free(b);
    // free(c);

    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);
}
