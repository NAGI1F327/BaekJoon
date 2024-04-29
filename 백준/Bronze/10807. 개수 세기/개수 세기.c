#include<stdio.h>
int main(){
    int n, array[100], v;
    int cnt = 0;
    
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&array[i]);
    }

    scanf("%d", &v);
    for (int j = 0; j < n; j++) {
        if(array[j] == v)
            cnt++;
    }
    printf("%d", cnt);
    return 0;
}