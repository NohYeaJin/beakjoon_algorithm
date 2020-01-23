#include <stdio.h>

int main(void) {
	int n;
	int i;
	int num;
	int sum;
	scanf_s("%d", &num);
	for (i = 0; i < num; i++) {
		scanf_s("%d", &n);
		sum += n;
	}
	printf("%d", sum);

}