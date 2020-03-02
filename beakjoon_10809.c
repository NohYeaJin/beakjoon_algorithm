#include <stdio.h>

int main(void) {
	int i;
	int j;
	int k;
	int n;
	int num = 97;
	int alp[26];
	int numarray[26];
	char name[101] = { NULL };
	//초기화가 꼭 필요!! 글자수가 100이라는 보장X
	for (i = 0; i < 26; i++) {
		alp[i] = num;
		num = num + 1;
	}
	scanf("%s", name);
	n = sizeof(name);
	for (j = 0; j < 26; j++) {
		for (k = 0; k < n; k++) {
			if (alp[j] == name[k]) {
				numarray[j] = k;
				break;
			}
			numarray[j] = -1;
		}
	}
	for (i = 0; i < 26; i++) {
		printf("%d ", numarray[i]);
	}
	printf("\n");
}