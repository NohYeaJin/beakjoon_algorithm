#include <stdio.h>
#include <string.h>

int main(void) {
	
	int num;
	int score = 0;
	int n;
	int i;
	int j;

	scanf("%d\n", &num);

	for (i = 0; i < num; i++) {
		char answer[100] = { NULL };
		gets(answer);
		n = strlen(answer);
		for (j = 0; j < n; j++) {
			if (answer[j] == 'O') {
				score = score + 1;
				if (answer[j + 1] == 'O')
					score = score + 1;
			}

		}
		printf("%d\n", score);
	}
	
	
	
}


		
	
	
	
