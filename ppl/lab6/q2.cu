#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

//each thread calculates the final position of its element by counting how many elements are less than it
__global__ void parallelSelectionSort(int*d_a,int*d_c,int s){
    int i=blockIdx.x*blockDim.x+threadIdx.x;
    int k=0;
    for(int j=0;j<s;j++){
        if((d_a[j]<d_a[i])||(d_a[j]==d_a[i]&&j>i))
            k++;
    }
    d_c[k]=d_a[i];
}

int main(){
    int n;
    printf("enter number of elements: ");
    scanf("%d",&n);
    int a[n],c[n];
    int *d_a,*d_c;

    cudaMalloc((void **)&d_a,n*sizeof(int));
    cudaMalloc((void **)&d_c,n*sizeof(int));

    printf("enter the elements: \n");
    for(int i=0;i<n;i++) scanf("%d",&a[i]);
    
    cudaMemcpy(d_a,a,n*sizeof(int),cudaMemcpyHostToDevice);
    parallelSelectionSort<<<1, n>>>(d_a,d_c,n);
    cudaMemcpy(c,d_c,n*sizeof(int),cudaMemcpyDeviceToHost);
    printf("sorted array: \n");
    for(int i=0;i<n;i++) 
        printf("%d ",c[i]);
        printf("\n"); 
    cudaFree(d_a);
    cudaFree(d_c);
}