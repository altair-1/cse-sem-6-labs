#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <string.h>

__device__ bool match_word(char* str, int idx, char* key, int keylen) {
    for (int i = 0; i < keylen; i++) {
        if (str[idx + i] != key[i]) {
            return false;
        }
    }
    return true;
}

__global__ void wordMatch(char* str, int len, char* key, int keylen, int *count) {
    int id = blockIdx.x * blockDim.x + threadIdx.x;
    if (id < len - keylen + 1) {
        if (match_word(str, id, key, keylen)) {
            atomicAdd(count, 1);
        }
    }
}

int main() {
    char str[100];
    printf("enter a sentence: ");
    scanf("%[^\n]%*c", str);
    int len = strlen(str);
    
    char key[20];
    printf("enter a word from the sentence: ");
    scanf("%[^\n]%*c", key);
    int keylen = strlen(key);
    
    int count = 0;
    char *d_str, *d_key;
    int *d_count;
    
    cudaMalloc((void**)&d_str, len * sizeof(char));
    cudaMalloc((void**)&d_key, keylen * sizeof(char));
    cudaMalloc((void**)&d_count, sizeof(int));
    
    cudaMemcpy(d_str, str, len * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_key, key, keylen * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_count, &count, sizeof(int), cudaMemcpyHostToDevice);

    wordMatch<<<ceil((float)len/256), 256>>>(d_str, len, d_key, keylen, d_count);
    cudaDeviceSynchronize();
    cudaMemcpy(&count, d_count, sizeof(int), cudaMemcpyDeviceToHost);
    printf("occurrences of the word '%s' in the sentence: %d\n", key, count);

    cudaFree(d_str);
    cudaFree(d_key);
    cudaFree(d_count);
    return 0;
}