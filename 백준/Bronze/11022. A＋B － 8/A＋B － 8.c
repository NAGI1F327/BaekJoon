#include <stdio.h>

int main() {
	int A, B, N;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++) {
		scanf("%d %d", &A, &B);
		printf("Case #%d: %d + %d = %d \n", i, A, B, A + B);
	}
	return 0;
}
