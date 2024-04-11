#include <stdio.h>

int main() {
	int A, B;

	while (scanf("%d %d", &A, &B) != EOF) {   // while(1)을 쓰면 무한루프를 돌게 되어 '출력초과' error 발생 (메모리 할당 범위를 넘어감)
		printf("%d \n", A + B);
	}
	return 0;
}

// 해결법 : EOF(End-of-File) 사용, 파일 끝, 즉, 데이터 입력이 없을 때 실행을 끝냄
// <stdio.h> 파일의 41행에 -1 값으로 정의되어 있는 상수이다
// 결국 사용자가 입력하는 두 정수가 EOF가 아닐 때 까지만 출력하도록 작성 
