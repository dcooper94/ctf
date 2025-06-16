
#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Enter access code: ");
    scanf("%s", input);
    if (strcmp(input, "coops{re_entry_block_01}") == 0) {
        printf("Access granted.\n");
    } else {
        printf("Access denied.\n");
    }
    return 0;
}
