#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

const int n = 1000;

__global__ void vector_addition(int *a, int *b, int *c) {
    int tid = (blockIdx.x * blockDim.x) + threadIdx.x;
    if(tid < n) c[tid] = a[tid] + b[tid];
}

int main() {
    int *d_a, *d_b, *d_c; // device copies
    int size = sizeof(int);
    
    cudaMalloc((void**)&d_a, n * size);
    cudaMalloc((void**)&d_b, n * size);
    cudaMalloc((void**)&d_c, n * size);

    int a[n], b[n], c[n];
    for (int i = 0; i < n; i++) {
        a[i] = i;        // a[i] = 0, 1, 2, ..., 999
        b[i] = i;        // b[i] = 0, 1, 2, ..., 999
    }

    cudaMemcpy(d_a, a, n * size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, n * size, cudaMemcpyHostToDevice);

    int block_size = 256;
    int grid_size = (n + block_size - 1) / block_size;  // Equivalent to ceil(n / 256)
    vector_addition<<<grid_size, block_size>>>(d_a, d_b, d_c);

    cudaError_t err = cudaGetLastError();
    if (err != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(err));
        return -1;
    }

    cudaMemcpy(c, d_c, n * size, cudaMemcpyDeviceToHost);

    printf("array after vector addition is: \n");
    for (int i = 0; i < 20; i++) {  
        printf("%d ", c[i]);
    }
    printf("...\n");

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    return 0;
}