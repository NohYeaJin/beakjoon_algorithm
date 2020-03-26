#include <stdio.h>
int main(void) {
	int num=0;
	int kg;
	scanf("%d", &kg);
	while (kg >= -2) {
		printf("%d", kg);
		if (kg == 0) {
			printf("%d", num);
		}
		else if (kg < 0) {
			printf("-1");
		}
		else if (kg >= 5) {
			kg = kg - 5;
			num = num + 1;
		}
		else if (kg >= 3) {
			kg = kg - 3;
			num = num + 1;
		}
	}
}