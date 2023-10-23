#include <stdio.h>
#include <opencv2/opencv.hpp>

#define WIDTH 640
#define HEIGHT 480
#define KERNEL_SIZE 5

// CUDA kernel for 2D convolution
__global__ void convolution2D(int *input, int *mask, int *output, int width, int height, int kernelSize)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < height && col < width)
    {
        int sum = 0;
        int offset = kernelSize / 2;

        for (int i = 0; i < kernelSize; i++)
        {
            for (int j = 0; j < kernelSize; j++)
            {
                int r = row + i - offset;
                int c = col + j - offset;

                if (r >= 0 && r < height && c >= 0 && c < width)
                {
                    sum += input[r * width + c] * mask[i * kernelSize + j];
                }
            }
        }

        output[row * width + col] = sum;
    }
}

int main()
{
    cv::Mat inputImage = cv::imread("input.jpg", cv::IMREAD_GRAYSCALE); // Load the input image
    int *d_input, *d_mask, *d_output;
    int input[HEIGHT][WIDTH], output[HEIGHT][WIDTH];
    int mask[KERNEL_SIZE][KERNEL_SIZE] = {{1, 0, 0, 0, 0}, {1, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, -1, 0}, {0, 0, 0, 0, -1}}; // Embossing kernel

    if (inputImage.empty())
    {
        printf("Could not open or find the image.\n");
        return -1;
    }

    // Convert the OpenCV image to a grayscale input array
    for (int i = 0; i < HEIGHT; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            input[i][j] = static_cast<int>(inputImage.at<uchar>(i, j));
        }
    }

    // Allocate memory on the device
    cudaMalloc((void **)&d_input, WIDTH * HEIGHT * sizeof(int));
    cudaMalloc((void **)&d_mask, KERNEL_SIZE * KERNEL_SIZE * sizeof(int));
    cudaMalloc((void **)&d_output, WIDTH * HEIGHT * sizeof(int));

    // Copy data from host to device
    cudaMemcpy(d_input, input, WIDTH * HEIGHT * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_mask, mask, KERNEL_SIZE * KERNEL_SIZE * sizeof(int), cudaMemcpyHostToDevice);

    // Define grid and block dimensions
    dim3 dimGrid((WIDTH + 15) / 16, (HEIGHT + 15) / 16);
    dim3 dimBlock(16, 16);

    // Launch the CUDA kernel
    convolution2D<<<dimGrid, dimBlock>>>(d_input, d_mask, d_output, WIDTH, HEIGHT, KERNEL_SIZE);

    // Copy the result back to the host
    cudaMemcpy(output, d_output, WIDTH * HEIGHT * sizeof(int), cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(d_input);
    cudaFree(d_mask);
    cudaFree(d_output);

    // Save the output image
    cv::Mat outputImage(HEIGHT, WIDTH, CV_8U);
    for (int i = 0; i < HEIGHT; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            outputImage.at<uchar>(i, j) = static_cast<uchar>(output[i][j]);
        }
    }
    cv::imwrite("output.jpg", outputImage);

    return 0;
}
