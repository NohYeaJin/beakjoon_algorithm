#include <stdio.h>
int main(void) {
	int must_price;
	int per_price;
	int per_cost;
	double x;
	int i;
	scanf("%d %d %d", &must_price, &per_price, &per_cost);
	if (per_price < per_cost) {
		 i = must_price / (per_cost - per_price);

		x = must_price % (per_cost - per_price);
		printf("%d", i + 1);
	}
	else {
		printf("-1");
	}
}