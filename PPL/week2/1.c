#include "mpi.h"
#include <stdio.h>
#include<string.h>
int main(int argc, char *argv[]){
    int rank,size,x;
    char c[] = "hello";
    //scanf("%s", &c[0]);
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if (rank == 0){
        fprintf(stdout,"Sending word : %s\n", c);
        fflush(stdout);
        MPI_Ssend(&c,strlen(c),MPI_CHAR,1,1,MPI_COMM_WORLD);
        MPI_Recv(&c, strlen(c), MPI_CHAR,1,1,MPI_COMM_WORLD, &status);
        fprintf(stdout, "Received word: %s", c);
        fflush(stdout);
    }
    else{
        MPI_Recv(&c, strlen(c), MPI_CHAR,0,1,MPI_COMM_WORLD, &status);
        for (int i = 0;c[i]!='\0';i=i+2){
            c[i] = c[i] - 32;
        }
        MPI_Ssend(&c,strlen(c),MPI_CHAR,0,1,MPI_COMM_WORLD);
    }
    MPI_Finalize();
    return 0;
}