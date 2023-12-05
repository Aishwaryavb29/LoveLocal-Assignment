#include <stdio.h>
#include <string.h>

int lengthOfLastWord(char *s) {
    int len = 0;
    int i = strlen(s) - 1;

    // Skip trailing spaces
    while (i >= 0 && s[i] == ' ')
        i--;

    // Count the length of the last word
    while (i >= 0 && s[i] != ' ') {
        len++;
        i--;
    }

    return len;
}

int main() {
    // Test cases
    char s1[] = "Hello World";
    printf("Output 1: %d\n", lengthOfLastWord(s1));

    char s2[] = " fly me to the moon ";
    printf("Output 2: %d\n", lengthOfLastWord(s2));

    char s3[] = "luffy is still joyboy";
    printf("Output 3: %d\n", lengthOfLastWord(s3));

    return 0;
}
