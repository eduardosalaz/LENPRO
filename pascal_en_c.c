#include <stdio.h>
long fun(int y)
{
    int z;
    long result = 1;
 
    for( z = 1 ; z <= y ; z++ )
        result = result*z;
 
    return ( result);
}
int main()
{
    int x, y, z, n;
    printf("Input the number of rows in Pascal's triangle: ");
    scanf("%d",&y);
    printf("Ingresar la base deseada: ");
    scanf("%d", &n);
    for ( x = 0 ; x < y ; x++ )
    {
        for ( z = 0 ; z <= ( y - x - 2 ) ; z++ )
            printf(" ");
        for( z = 0 ; z <= x ; z++ )
            printf("%ld ",fun(x) * n/ (fun(z)*fun(x-z)));
 
        printf("\n");
    }
    return 0;
}
