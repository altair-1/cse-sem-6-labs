#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <string.h>

__global__ void buildRS(char* s, char* rs, int len) {
    int i = threadIdx.x;
    int offset = 0;
    for (int j = 0; j < i; j++) {
        offset += len - j;
    }
    for (int j = 0; j < len - i; j++) {
        rs[offset + j] = s[j];
    }
}

int main() {
    char s[100];
    printf("enter input string S: ");
    scanf("%s", s);
    int len = strlen(s);

    int rs_len = len * (len + 1) / 2;  
    char* rs = (char*)malloc((rs_len + 1) * sizeof(char));  
    rs[rs_len] = '\0';

    char *d_s, *d_rs;
    cudaMalloc((void**)&d_s, len * sizeof(char));
    cudaMalloc((void**)&d_rs, rs_len * sizeof(char));

    cudaMemcpy(d_s, s, len * sizeof(char), cudaMemcpyHostToDevice);

    buildRS<<<1, len>>>(d_s, d_rs, len);
    cudaDeviceSynchronize();

    cudaMemcpy(rs, d_rs, rs_len * sizeof(char), cudaMemcpyDeviceToHost);

    printf("output string RS: %s\n", rs);

    cudaFree(d_s);
    cudaFree(d_rs);
    free(rs);

    return 0;
}