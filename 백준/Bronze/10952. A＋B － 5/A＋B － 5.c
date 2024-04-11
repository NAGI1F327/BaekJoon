#include <stdio.h>

int main() {
	int A, B;

	while (1) {   // 무한 while 루프
		scanf("%d %d", &A, &B);
		if (A, B == 0)   // A, B의 값이 0이면 while 루프 종료
			break;   // 루프 바깥으로 빠져나감
		printf("%d \n", A + B);
		
	}
	return 0;
}