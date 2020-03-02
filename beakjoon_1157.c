#include <stdio.h>
#include <string.h>

int main(void) {
	char words[1000001] = { 0, };
	int alp[26] = { 0, }; //이거 int무조건!!!!
	int n=0;
	int i=0;
	int j=0;
	int max=0;
	int maxindex = 0;
	scanf("%s", words);
	n = strlen(words);
	for (i = 0; i < n; i++) {
		if (words[i] > 96)
			j = words[i] - 97;

		else
			j = words[i] - 65;

		alp[j] = alp[j] + 1;

	}
	max = alp[0];
	for (i = 1; i < 26; i++) {
		if (alp[i] > max) {
			max = alp[i];
			maxindex = i;
		}
	}
	for (i = 0; i < 26; i++) {
		if ((maxindex != i) && (max == alp[i])) {
			maxindex = -2;
			break;
			}
		}
	printf("%c", maxindex + 65);
}