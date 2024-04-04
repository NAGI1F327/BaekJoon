#include <stdio.h>

int main() {
	int H, M, m;

	scanf("%d %d %d", &H, &M, &m);

	H += m / 60;
	M += m % 60;

	if (M >= 60) {
		++H;
		M -= 60;
	}
	if (H >= 24) {
		H -= 24;
	}
	printf("%d %d", H, M);

	return 0;
}
