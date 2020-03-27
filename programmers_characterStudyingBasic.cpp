#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool solution(const char* s) {

	bool answer = true;;
	int flag = 0;
	int num;
	if (strlen(s) != 4 && strlen(s) != 6) {
		answer = false;
		printf("%d", strlen(s));
		return answer;
	}
	for (int i = 0; i < strlen(s); i++) {
		num = (int)(s[i]);
		if (num > 57 || num < 48) {
			flag = 1;
		}
	}
	if (flag == 0) {
		return answer;
	}
	else {
		answer = false;
		return answer;
	}
}

int main(void) {
	printf("%d",solution("1234"));

}