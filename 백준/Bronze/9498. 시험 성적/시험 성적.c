#include <stdio.h>

int main() {
	int score = 0;
	scanf("%d", &score);

	if (90 <= score && score <= 100)
		printf("A \n", score);
	else if (80 <= score && score <= 89)
		printf("B \n", score);
	else if (70 <= score && score <= 79)
		printf("C \n", score);
	else if (60 <= score && score <= 69)
		printf("D \n", score);
	else
		printf("F \n", score);

	return 0;
}
