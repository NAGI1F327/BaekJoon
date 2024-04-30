#include<stdio.h>
int main(){
    int N, X, array[10000];

    scanf("%d %d", &N, &X);

    for (int i = 0; i < N; i++) {
        scanf("%d", &array[i]);
            if(array[i] < X)
                printf("%d ", array[i]);
    }
    return 0;
}