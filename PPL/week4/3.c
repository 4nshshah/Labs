#include "mpi.h"
#include <stdio.h>

int main(int argc, char *argv[])
{
    int rank, size, a[3][3], find, b[3], sum = 0, final;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0)
    {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                scanf("%d", &a[i][j]);
        printf("Enter element to be found:\n");
        scanf("%d", &find);
    }
    MPI_Bcast(&find, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(a, 3, MPI_INT, b, 3, MPI_INT, 0, MPI_COMM_WORLD);

    // fprintf(stdout, "\nReceived %d", find);
    // fflush(stdout);

    for (int i = 0; i < 3; i++)
    {
        if (b[i] == find)
        {
            sum += 1;
        }
    }
    MPI_Reduce(&sum, &final, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0)
    {
        fprintf(stdout, "\nTotal occurances: %d\n", final);
    }
    MPI_Finalize();
}