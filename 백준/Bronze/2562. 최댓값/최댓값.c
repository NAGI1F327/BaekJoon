#include <stdio.h>

int main() {
    int array[9] = {0};
    int max = 0, p = 0;
	
    for (int i = 0; i < 9; i++) {
        scanf("%d", &array[i]);
        if (max < array[i]) {
            max = array[i];
            p = i + 1;
        }
    }
	
    printf("%d\n%d", max, p);
    return 0;
}