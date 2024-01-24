#include "mpi.h"
#include<stdio.h>
int main(int argc, char *argv[])
{
	int rank, size;
	char word[]="HeLLO";
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if(word[rank]>='a' && word[rank]<='z')
	{
		word[rank]-=32;
		printf("%s\n", word);
	}
	else
	{
		word[rank]+=32;
		printf("%s\n", word);
	}
	MPI_Finalize();
	return 0;
}