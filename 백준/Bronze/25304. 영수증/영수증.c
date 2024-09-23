#include <stdio.h>

int main() {
	int X, N, a, b, i;
    
	scanf("%d \n %d", &X, &N);

	for (i = 0; i < N; i++) {
		scanf("%d %d", &a, &b);
		X -= a * b;
	}
	if (X == 0)
		printf("Yes");
	else
		printf("No");

	return 0;
}