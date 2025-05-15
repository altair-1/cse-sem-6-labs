#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	int rank, size;
	int a = atoi (argv[1]); 
	int b = atoi (argv[2]);
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if(rank == 0)
		printf("%d + %d = %d\n", a, b, a+b);
	else if(rank == 1)
		printf("%d - %d = %d\n", a, b, a-b);
	else if(rank == 2)
		printf("%d * %d = %d\n", a, b, a*b);
	else if(rank == 3)
		printf("%d / %d = %d\n", a, b, a/b);
	MPI_Finalize();
	return 0;
}