#include <stdio.h>

int main(void) {
	int test_num = 0; 
	int std_num = 0; 
	int std_score = 0;
	int total = 0; 
	float average = 0; 
	float score[1001] = { 0 };
	int aver_up = 0; 
	double percentage[1001] = { 0 };
	char per = '%';
	int i = 0;
	int j = 0;

	scanf("%d\n", &test_num);
	for (i = 0; i < test_num; i++) {
		scanf("%d", &std_num);
		for (j = 0; j < std_num; j++) {
			scanf("%d", &std_score);
			total = total + std_score;
			score[j] = std_score;
		}
		average = total / std_num;
		for (j = 0; j < std_num; j++) {
			printf("%d lal", score[j]);
			if (score[j] > average) {
				aver_up = aver_up + 1;
			}
			
		}
		percentage[i] = (100 * (aver_up*(1.0) / std_num));
		//printf("std %d", aver_up);
	}
	for (i = 0; i < test_num; i++) {
		//printf("%.3f%%\n", percentage[i]);
	}
	return 0;
}







