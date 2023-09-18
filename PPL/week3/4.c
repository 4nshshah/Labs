#include <mpi.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int rank, size, N, A[10], B[10], chunk;
    char c[10];
    char str[20];
    int nv = 0;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0)
    {
        N = size;
        fprintf(stdout, "Enter string:\n");
        fflush(stdout);
        scanf("%s", str);
        fprintf(stdout, "Entered string: %s\n", str);
        fflush(stdout);
        chunk = strlen(str) / N;
    }
    MPI_Bcast(&chunk, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(str, chunk, MPI_CHAR, c, chunk, MPI_CHAR, 0, MPI_COMM_WORLD);
    fprintf(stdout, "I have recieved %s in process %d\n", c, rank);
    fflush(stdout);

    for (int i = 0; i < chunk; i++)
    {
        if (c[i] != 'a' && c[i] != 'e' && c[i] != 'i' && c[i] != 'o' && c[i] != 'u')
        {
            nv += 1;
        }
    }

    MPI_Gather(&nv, 1, MPI_INT, B, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        fprintf(stdout, "The result gathered in the root:\n");
        fflush(stdout);
        for (int i = 0; i < N; i++)
        {
            fprintf(stdout, "%d\t", B[i]);
            fflush(stdout);
        }
        int nv1 = 0;
        for (int i = 0; i < strlen(str); i++)
        {
            if (str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u')
            {
                nv1 += 1;
            }
        }
        fprintf(stdout, "\nThe sum gathered in the root: %d\n", nv1);
        fflush(stdout);
    }

    MPI_Finalize();
    return 0;
}