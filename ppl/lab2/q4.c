#include "mpi.h"
#include <stdio.h>

int main(int argc, char* argv[]){
    int rank,size,x;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if(rank==0){
        printf("enter a number in master process: ");
        scanf("%d",&x);
        MPI_Send(&x, 1, MPI_INT, 1,1, MPI_COMM_WORLD);
        fprintf(stdout, "sent %d from process 0 to process 1\n",x);
        fflush(stdout);
        MPI_Recv(&x, 1, MPI_INT, size-1, 2,MPI_COMM_WORLD, &status);
        printf("process %d receives %d from process %d\n", rank, x, size);
    }
    else if(rank<size-1){
        MPI_Recv(&x, 1, MPI_INT, rank-1, 1,MPI_COMM_WORLD, &status);
        printf("process %d receives %d from process %d\n", rank, x, rank-1);
        x++;
        MPI_Send(&x, 1, MPI_INT, rank+1, 1, MPI_COMM_WORLD);
        printf("process %d sends %d to process %d\n", rank, x, rank+1);
    }
    else{
        MPI_Recv(&x, 1, MPI_INT, rank-1, 1,MPI_COMM_WORLD, &status);
        printf("process %d receives %d from process %d\n", rank, x, rank-1);
        MPI_Send(&x, 1, MPI_INT, 0, 2, MPI_COMM_WORLD);
        printf("process %d sends num %d to process 0\n", rank, x);
        fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}