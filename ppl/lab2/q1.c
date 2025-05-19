#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <mpi.h>

#define maxlen 100

void toggle_case(char* word) {
    for (int i = 0; word[i] != '\0'; i++) {
        if (isupper(word[i])) {
            word[i] = tolower(word[i]);
        } else if (islower(word[i])) {
            word[i] = toupper(word[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    char word[maxlen];
    if (rank == 0) {
        printf("process 0: enter a word to send: ");
        fgets(word, maxlen, stdin);
        word[strcspn(word, "\n")] = '\0';
        MPI_Ssend(word, strlen(word) + 1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
        printf("process 0: sent word \"%s\" to process 1\n", word);
        MPI_Recv(word, maxlen, MPI_CHAR, 1, 1, MPI_COMM_WORLD, &status);
        printf("process 0: received modified word \"%s\" from process 1\n", word);
    }
    else if (rank == 1) {
        MPI_Recv(word, maxlen, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &status);
        printf("process 1: received word \"%s\" from process 0\n", word);
        toggle_case(word);
        printf("process 1: toggled word to \"%s\"\n", word);
        MPI_Ssend(word, strlen(word) + 1, MPI_CHAR, 0, 1, MPI_COMM_WORLD);
        printf("process 1: sent modified word \"%s\" back to process 0\n", word);
    }
    MPI_Finalize();
    return 0;
}