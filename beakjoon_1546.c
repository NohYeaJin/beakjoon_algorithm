#include <stdio.h>
int main() {
	int i;
	int subNum;
	double newAverage = 0;
	int subscore;
	int score[1000];
	int maxnum;

	scanf_s("%d", &subNum);
	scanf_s("%d", &subscore);
	score[0] = subscore;
	maxnum = score[0];
	for (i = 1; i < subNum; i++) {
		scanf_s("%d", &subscore);
		score[i] = subscore;
		if (maxnum < score[i]) {
			maxnum = score[i];
		}

	}
	for (i = 0; i < subNum; i++) {
		newAverage += (((float)score[i] / maxnum) * 100);
	}
	newAverage = newAverage / (float)subNum;
	printf("%.2f", newAverage);
}

