#include "mpi.h"
#include <stdio.h>

float function(float x)
{
    return 4 / (1 + (x * x));
}

int main(int argc, char *argv[])
{
    int rank, size, value, n;
    float h, sum, x, pi = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0)
    {
        printf("Enter n:\n");
        scanf("%d", &n);
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    h = 1 / (float)n;
    sum = 0.0;
    for (int i = rank + 1; i <= n; i += size)
        sum += h * function(h * ((float)i - 0.5));
    MPI_Reduce(&sum, &pi, 1, MPI_FLOAT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0)
    {
        fprintf(stdout, "Value of pi : %f", pi);
        fflush(stdout);
    }
    MPI_Finalize();
}