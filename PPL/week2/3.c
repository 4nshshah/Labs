#include<mpi.h>
#include<stdio.h>
// #define S 512

int main(int argc, char *argv[])
{
    int rank, size, x, S=512;
    int a[10] = {10,20,30,40,50,60,70,80,90,100};
    int buf[S];
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    MPI_Buffer_attach(buf,S);
    if(rank==0){
        fprintf(stdout,"This is the master process, reading n values...\n");
        fflush(stdout);
        for (int i = 0; i < size; i++)
        {
            fprintf(stdout,"%d\n", a[i]);
        }
        
        for(int i=1; i<size; i++){
            MPI_Bsend(&a[i],1,MPI_INT,i,1,MPI_COMM_WORLD);
            fprintf(stdout,"I have sent %d from process 0\n",a[i]);
            fflush(stdout);
        }
        
    }
    
    else{
        
       MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"I have received %d in process %d\n",x, rank);
        int result;
        if(rank %2==0)
        result = x*x;
        else
        result = x*x*x;
        fprintf(stdout,"Result: %d Rank: %d\n", result, rank);
        fflush(stdout); 
    }
    MPI_Buffer_detach(&buf,&S);
    MPI_Finalize();
    return 0;
}