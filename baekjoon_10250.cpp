#include <stdio.h>

int main(void) {
	int testcase = 0;
	scanf("%d", &testcase);
	int a;
	int b;
	int c;
	int num;
	for (int i = 0; i < testcase; i++) {
		scanf("%d %d %d", &a, &b, &c);
		num = c / a;
		if (c%a > 0) {
			if (num >= 9) {
				printf("%d%d\n", c%a, num + 1);
			}
			else {
				printf("%d0%d\n", c%a, num + 1);
			}
		}
		else {
			if (num > 9) {
				printf("%d%d\n", a, num);
			}
			else {
				printf("%d0%d\n", a, num);
			}
			
		}
	}
}