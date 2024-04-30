#include<stdio.h>
int main(){
    int N, array[100], v;
    int cnt = 0;
    
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d",&array[i]);
    }

    scanf("%d", &v);
    for (int j = 0; j < N; j++) {
        if(array[j] == v)
            cnt++;
    }
    printf("%d", cnt);
    return 0;
}