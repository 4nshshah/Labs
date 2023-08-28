#include "mpi.h"
#include <stdio.h>

int main(int argc, char *argv[])
{
    int rank, size, a, total, n, my;
    MPI_Init(&argc, &argv);
    // MPI_Errhandler_set(MPI_COMM_WORLD, MPI_ERRORS_RETURN);
    MPI_Comm_rank(my, &rank);
    // MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    a = rank + 1;
    MPI_Scan(&a, &n, 1, MPI_INT, MPI_PROD, MPI_COMM_WORLD);
    // fprintf(stdout, "\nfactorial = %d\n",n);
    // fflush(stdout);
    MPI_Reduce(&n, &total, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0)
    {
        fprintf(stdout, "\nSum of %d factorials = %d\n", size, total);
        fflush(stdout);
    }

    MPI_Finalize();
}