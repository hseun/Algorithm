#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int top = -1, length = strlen(s);
    for(int i = 0; i < length; i++) {
        if(s[i] == '(')
            top++;
        else if(top != -1 && s[i] == ')')
            top--;
        else
            return false;
    }
    if(top == -1)
        return true;
    else
        return false;
}