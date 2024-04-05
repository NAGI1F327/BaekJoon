#include <stdio.h>

int main() {
	int i, j, sum = 0;
	scanf("%d", &j);

	for (i = 1; i <= j; i++) {
		sum = sum + i;
	}
	printf("%d", sum);

	return 0;
}