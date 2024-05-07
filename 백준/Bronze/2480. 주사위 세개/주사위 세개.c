#include <stdio.h>
#define MAX(x, y) ((x) > (y) ? (x) : (y))
// 매크로 함수 #define
// 조건연산자[ (조건) ? 수식1 : 수식2 ]

int main() {
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c)   // 3개 같을 때
		printf("%d \n", 10000 + a * 1000);
	else if (a == b || a == c)  // 2개 같을 때
		printf("%d \n", 1000 + a * 100);
	else if (b == c)  // 2개 같을 때 남은 경우의 수
		printf("%d \n", 1000 + b * 100);
	else   // 전부 다를 때
		printf("%d \n", MAX(MAX(a, b), c) * 100);
	return 0;
}