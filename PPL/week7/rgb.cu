#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>

#define CHANNELS 3

__global__ void rgbToGray(unsigned char *inputImage, unsigned char *outputImage, int width, int height)
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height)
    {
        int grayOffset = y * width + x;
        int rgbOffset = grayOffset * CHANNELS;

        unsigned char r = inputImage[rgbOffset];
        unsigned char g = inputImage[rgbOffset + 1];
        unsigned char b = inputImage[rgbOffset + 2];

        outputImage[grayOffset] = 0.299f * r + 0.587f * g + 0.114f * b;
    }
}

int main()
{
    // Load RGB image
    unsigned char *h_inputImage;
    int width, height;
    // ... code to load the input image ...

    // Allocate memory in GPU
    unsigned char *d_inputImage;
    unsigned char *d_outputImage;
    size_t imageSize = width * height * CHANNELS * sizeof(unsigned char);
    cudaMalloc((void **)&d_inputImage, imageSize);
    cudaMalloc((void **)&d_outputImage, width * height * sizeof(unsigned char));

    // Copy input image to GPU
    cudaMemcpy(d_inputImage, h_inputImage, imageSize, cudaMemcpyHostToDevice);

    // Set up grid and block dimensions
    dim3 dimBlock(16, 16);
    dim3 dimGrid((width + dimBlock.x - 1) / dimBlock.x, (height + dimBlock.y - 1) / dimBlock.y);

    // Launch kernel
    rgbToGray<<<dimGrid, dimBlock>>>(d_inputImage, d_outputImage, width, height);

    // Copy output image from GPU
    unsigned char *h_outputImage = (unsigned char *)malloc(width * height * sizeof(unsigned char));
    cudaMemcpy(h_outputImage, d_outputImage, width * height * sizeof(unsigned char), cudaMemcpyDeviceToHost);

    // ... code to save the output image ...

    // Free memory
    cudaFree(d_inputImage);
    cudaFree(d_outputImage);
    free(h_outputImage);

    return 0;
}