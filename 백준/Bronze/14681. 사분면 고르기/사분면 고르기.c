#include <stdio.h>

int main() {
	int x, y;
	
	scanf("%d %d", &x, &y);
	
	if (x > 0 && y > 0)
		printf("1", x, y);
	else if (x < 0 && y>0)
		printf("2", x, y);
	else if (x < 0 && y < 0)
		printf("3", x, y);
	else
		printf("4", x, y);
	return 0;
}
