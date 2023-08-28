#include<mpi.h>
#include<stdio.h>

int main(int argc, char *argv[])
{
    int rank, size, x;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if(rank==0){
        fprintf(stdout,"This is the master process, enter a number...\n");
        fflush(stdout);
        scanf("%d", &x);
        MPI_Send(&x,1,MPI_INT,1,1,MPI_COMM_WORLD);
        fprintf(stdout,"I have sent %d from process 0\n",x);
        fflush(stdout);
        MPI_Recv(&x,1,MPI_INT,2,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"I have received %d in process %d\n",x, rank);
    }
    else if(rank==size-1){
       MPI_Recv(&x,1,MPI_INT,MPI_ANY_SOURCE,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"I have received %d in process %d\n",x, rank);
        int m = x+1;
        MPI_Send(&m,1,MPI_INT,0,1,MPI_COMM_WORLD);
        fprintf(stdout,"I have sent %d from process 1\n",m);
        fflush(stdout); 
    } else {
       MPI_Recv(&x,1,MPI_INT,MPI_ANY_SOURCE,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"I have received %d in process %d\n",x, rank);
        int m = x+1;
        MPI_Send(&m,1,MPI_INT,rank+1,1,MPI_COMM_WORLD);
        fprintf(stdout,"I have sent %d from process 2\n",m);
        fflush(stdout); 
    }
    MPI_Finalize();
    return 0;
}