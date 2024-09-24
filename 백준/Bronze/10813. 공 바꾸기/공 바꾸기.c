#include<stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int Box[N + 1];
    for (int i = 1; i <= N; i++) {
        Box[i] = i;
    }
    
    for (int m = 0; m < M; m++) {
        int i, j;
        scanf("%d %d", &i, &j);
        int temp = Box[i];
        Box[i] = Box[j];
        Box[j] = temp;
    }
    
    for (int i = 1; i <= N; i++) {
        printf("%d ", Box[i]);
    }
    
    return 0;
}