#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int Box[N];
    for (int i = 0; i < N; i++) {
        Box[i] = 0;
    }
    
    for (int a = 0; a < M; a++) {
        int i, j, k;
        scanf("%d %d %d", &i, &j, &k);
        
        for (int b = i - 1; b < j; b++) {
            Box[b] = k;
        }
    }
    
    for (int c = 0; c < N; c++) {
        printf("%d ", Box[c]);
    }
    
    return 0;
}