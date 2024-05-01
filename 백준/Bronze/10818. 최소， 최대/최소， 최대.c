#include<stdio.h>
int main(){
    int N, min = 1000000, max = -1000000;
    scanf("%d", &N);
    int array[N];
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &array[i]);
        if(min > array[i])
            min = array[i];
        if(max < array[i])
            max = array[i];
    }
    printf("%d %d", min, max);
    return 0;
}