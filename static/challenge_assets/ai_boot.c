#include <stdio.h>
#include <string.h>

void unlock(char *input) {
    unsigned char obf[] = {33, 45, 45, 50, 49, 57, 48, 39, 29, 39, 44, 54, 48, 59, 29, 32, 46, 45, 33, 41, 29, 114, 115, 63, 0};
    char decoded[64];
    int i;
    for (i = 0; obf[i] != 0; i++) {
        decoded[i] = obf[i] ^ 0x42;
    }
    decoded[i] = '\0';

    if (strcmp(input, decoded) == 0) {
        puts("Access granted.");
    } else {
        puts("Access denied.");
    }
}

int main() {
    char buffer[64];
    printf("Enter access code: ");
    scanf("%63s", buffer);
    unlock(buffer);
    return 0;
}
