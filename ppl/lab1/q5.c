#include <stdio.h>
#include <mpi.h>

long long factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main(int argc, char *argv[]){
	int fib[15] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377};
	int rank, size;
	MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank % 2 == 0){
		printf("rank %d (even)\nfactorial of %d = %d\n", rank, rank, factorial(rank));
	}
	else{
		printf("rank %d (odd)\nfibonacci number = %d\n", rank, fib[rank]);
	}
    MPI_Finalize();
    return 0;
}