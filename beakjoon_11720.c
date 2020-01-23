#include<stdio.h>
int main(void) {
	int n;
	int i;
	int sum;
	char num[100];
	scanf("%d", &n);
	scanf("%s", num);
	for (i = 0; i < n; i++) {
		sum = sum + (num[i] - '0');
	}
	printf("%d", sum);
}