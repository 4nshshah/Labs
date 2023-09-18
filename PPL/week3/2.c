#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    int rank, size, N, M;
    int A[10];
    float B[10];
    int c[10];
    float avg, sum1 = 0, avg1;
    int sum = 0;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0)
    {
        N = size;
        fprintf(stdout, "Enter M:\n");
        fflush(stdout);
        scanf("%d", &M);
        fprintf(stdout, "Enter %d values:\n", N * M);
        fflush(stdout);
        for (int i = 0; i < N * M; i++)
        {
            scanf("%d", &A[i]);
        }
    }
    MPI_Bcast(&M, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(A, M, MPI_INT, c, M, MPI_INT, 0, MPI_COMM_WORLD);

    for (int i = 0; i < M; i++)
    {
        fprintf(stdout, "I have recieved %d in process %d\n", c[i], rank);
        fflush(stdout);
    }
    for (int i = 0; i < M; i++)
    {
        sum += c[i];
    }
    avg = sum / M;
    MPI_Gather(&avg, 1, MPI_FLOAT, B, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        fprintf(stdout, "The result gathered in the root:\n");
        fflush(stdout);
        for (int i = 0; i < N; i++)
        {
            fprintf(stdout, "%f\t", B[i]);
            fflush(stdout);
        }
        for (int i = 0; i < N; i++)
        {
            sum1 += B[i];
        }
        fprintf(stdout, "\nThe sum gathered in the root: %f\n", sum1);
        fflush(stdout);
        avg1 = sum1 / (N * M);
        fprintf(stdout, "\nThe average gathered in the root: %f\n", avg1);
        fflush(stdout);
    }

    MPI_Finalize();
    return 0;
}