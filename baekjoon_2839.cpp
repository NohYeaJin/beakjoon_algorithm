#include <stdio.h>
int main(void) {
	int num = 0;
	int kg=0;
	int check = 0;
	int num2 = 0;
	scanf("%d", &kg);
	num2 = kg;
	while (kg > 0) {
		if (kg >= 5) {
			kg = kg - 5;
			num = num + 1;			
		}
		else if (kg >= 3) {
			kg = kg - 3;
			num = num + 1;
		}
		else if (kg < 3) {
			for(int i = 0;i<(num2/5);i++){
				kg = kg + 5;
				if (kg % 3 == 0) {
					num = num + 1+i;
					check = 1;
					break;
				}

			}
			if (check != 1) {
				num = -1;
				break;
			}
			else {
				break;
			}
		}
	}
	printf("%d", num);
	return 0;
}