#include <mpi.h>
#include <stdio.h>
#include <math.h>

// int pow(int x,  int rank){
//     return x**rank;
// }

int main(int argc, char *argv[])
{
    int x = 5;
    int rank;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    printf("Rank: %d, pow(%d, %d) = %f\n", rank, x, rank, pow(x, rank));
    MPI_Finalize();
    return 0;
}