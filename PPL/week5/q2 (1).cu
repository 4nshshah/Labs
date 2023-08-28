#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

// Define the size of the vectors
#define N 1024

// CUDA kernel to add two vectors
__global__ void vecAdd(float *a, float *b, float *c) {
  // Get the global thread ID
  int id = blockIdx.x * blockDim.x + threadIdx.x;

  // Make sure we do not go out of bounds
  if (id < N) {
    c[id] = a[id] + b[id];
  }
}

// Main function
int main() {
  // Allocate memory for the vectors on the host
  float *h_a = (float *)malloc(N * sizeof(float));
  float *h_b = (float *)malloc(N * sizeof(float));
  float *h_c = (float *)malloc(N * sizeof(float));

  // Initialize the vectors
  for (int i = 0; i < N; i++) {
    h_a[i] = i;
    h_b[i] = i * 2;
  }

  // Allocate memory for the vectors on the device
  float *d_a, *d_b, *d_c;
  cudaMalloc(&d_a, N * sizeof(float));
  cudaMalloc(&d_b, N * sizeof(float));
  cudaMalloc(&d_c, N * sizeof(float));

  // Copy the vectors from the host to the device
  cudaMemcpy(d_a, h_a, N * sizeof(float), cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, h_b, N * sizeof(float), cudaMemcpyHostToDevice);

  // Calculate the number of blocks
  int numBlocks = N / 256;
  if (N % 256 != 0) {
    numBlocks++;
  }

  // Launch the kernel
  vecAdd<<<numBlocks, 256>>>(d_a, d_b, d_c);

  // Copy the result back from the device to the host
  cudaMemcpy(h_c, d_c, N * sizeof(float), cudaMemcpyDeviceToHost);

  // Print the result
  for (int i = 0; i < N; i++) {
    printf("%f\n", h_c[i]);
  }

  // Free the memory on the host
  free(h_a);
  free(h_b);
  free(h_c);

  // Free the memory on the device
  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);

  return 0;
}