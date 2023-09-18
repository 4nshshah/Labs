#include <mpi.h>
#include <stdio.h>

int fibb(int x)
{
    int t1 = 0;
    int t2 = 1;
    if (x == 1)
    {
        printf("Fibboniaci Nubmer: %d\n", t1);
        return 0;
    }
    if (x == 2)
    {
        printf("Fibboniaci Nubmer: %d\n", t2);
        return 0;
    }
    int nextTerm = t1 + t2;
    // printf("First two terms: %d %d\n", t1, t2);
    for (int i = 3; i <= x; i++)
    {

        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
    }
    printf("Fibboniaci Nubmer: %d\n", nextTerm);
}

int fact(int x)
{
    int ans = 1;
    for (int i = 2; i <= x; i++)
    {
        ans *= i;
    }
    printf("Factorial = %d\n", ans);
}

int main(int argc, char *argv[])
{
    int rank;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank % 2 == 0)
    {
        printf("Rank: %d so Factorial\n", rank);
        fact(rank);
    }
    else
    {
        printf("Rank: %d so Fibonacci\n", rank);
        fibb(rank);
    }
    MPI_Finalize();
    return 0;
}