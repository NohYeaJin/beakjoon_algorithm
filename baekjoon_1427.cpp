#include <stdio.h>
#include <string.h>

int main(void) {
	int max = 0;
	int num;
	int num2[10];
	int i = 0;
	int num3 = 10;
	scanf("%d",&num);
	while (num >= 10) {
		num2[i] = num % num3;
		num = num / num3;
		i++;

	}
	num2[i] = num;
	for (int j = 0; j <= i; j++) {
		for (int k = 0; k < (i - j); k++) {
			if (num2[k+1] > num2[k]) {
				max = num2[k];
				num2[k] = num2[k+1];
				num2[k+1] = max;
			}
		}
	}

	for (int f = 0; f <= i; f++) {
		printf("%d", num2[f]);
	}
}