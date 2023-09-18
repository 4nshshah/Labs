#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    char c[5] = "HELLO";
    int rank;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    c[rank] = c[rank] + 32;
    printf("Rank: %d\n", rank);
    printf("%s\n", c);
    MPI_Finalize();
    return 0;
}