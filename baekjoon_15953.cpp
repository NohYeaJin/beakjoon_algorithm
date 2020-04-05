#include <stdio.h>
#include <stdlib.h>
int prize1(int rank) {
	int total;
	int money[22] = { 0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10 };
	if (rank > 21) {
		total = 0;
	}
	else {
		total = money[rank];
	}

	return total;
}

int prize2(int rank) {
	int total;
	int money[32] = {0, 512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32 };
	if (rank > 31) {
		total = 0;
	}
	else {
		total = money[rank];
	}
	return total;
}


int main(void) {
	int numcase = 0;
	int rank1 = 0;
	int rank2 = 0;
	int total_prize = 0;
	scanf("%d", &numcase);
	for (int i = 0; i < numcase; i++) {
		scanf("%d %d", &rank1, &rank2);
		total_prize = (prize1(rank1) + prize2(rank2))*10000;
		printf("%d\n", total_prize);
	}
}