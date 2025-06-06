#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

void ErrorHandler(int err_code) {
    if(err_code != MPI_SUCCESS) {
        char error_string[BUFSIZ];
        int length_err_string, err_class;
        MPI_Error_class(err_code, &err_class);
        MPI_Error_string(err_code, error_string, &length_err_string);
        printf("error: %d %s\n", err_class, error_string);
    }
}

int main(int argc, char* argv[]) {
    int rank, size, fact=1, factsum, i, err_code;
    MPI_Init(&argc, &argv);
    MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    err_code = MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank == 0)
        ErrorHandler(err_code);
    int sendVal = rank+1;
    err_code = MPI_Scan(&sendVal, &fact, 1, MPI_INT, MPI_PROD, MPI_COMM_WORLD);
    if(rank == 0)
        ErrorHandler(err_code);
    err_code = MPI_Scan(&fact, &factsum, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    if(rank == 0)
        ErrorHandler(err_code);
    if(rank == size - 1)
        printf("sum of all factorials till %d! = %d\n", rank+1, factsum);
    MPI_Finalize();
    exit(0);
}