#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <string.h>

__global__ void occur(char *a, char *p, int *count, int n)
{
    int id = threadIdx.x;
    int c = 0;
    for (int i = id; i < id + n; i++)
        if (a[i] != p[i - id])
            c += 1;
    if (c == 0)
        atomicAdd(count, 1);
}

int main()
{
    char hA[100], *dA, hB[100], *dB;
    int c = 0;
    int *count = &c, result, *dC;
    printf("Enter the string and pattern:\n");
    scanf("%s", hA);
    printf("Enter the string and pattern:\n");
    scanf("%s", hB);

    cudaMalloc((void **)&dA, strlen(hA) * sizeof(char));
    cudaMalloc((void **)&dB, strlen(hB) * sizeof(char));
    cudaMalloc((void **)&dC, sizeof(int));

    cudaMemcpy(dA, hA, strlen(hA) * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(dB, hB, strlen(hB) * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(dC, count, sizeof(int), cudaMemcpyHostToDevice);
    int n = strlen(hA) / strlen(hB);
    occur<<<1, n>>>(dA, dB, dC, n);
    cudaMemcpy(&result, dC, sizeof(int), cudaMemcpyDeviceToHost);
    printf("Count:%d\n", result);
}