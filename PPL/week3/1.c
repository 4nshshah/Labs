#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    int rank, size, N, A[10], B[10], c;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0)
    {
        N = size;
        fprintf(stdout, "Enter %d values:\n", N);
        fflush(stdout);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &A[i]);
        }
    }
    MPI_Scatter(A, 1, MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);
    fprintf(stdout, "I have recieved %d in process %d\n", c, rank);
    fflush(stdout);

    int fact = 1;
    for (int i = 1; i <= c; i++)
    {
        fact *= i;
    }

    MPI_Gather(&fact, 1, MPI_INT, B, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        fprintf(stdout, "The result gathered in the root:\n");
        fflush(stdout);
        for (int i = 0; i < N; i++)
        {
            fprintf(stdout, "%d\t", B[i]);
            fflush(stdout);
        }
        int sum = 0;
        for (int i = 0; i < N; i++)
        {
            sum += B[i];
        }
        fprintf(stdout, "\nThe sum gathered in the root: %d\n", sum);
        fflush(stdout);
    }

    MPI_Finalize();
    return 0;
}