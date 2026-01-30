/*
 * ARTEMIS Backup Tool - Intentionally Vulnerable for CTF
 * This tool has a command injection vulnerability for educational purposes
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    char command[256];
    char filename[128];

    printf("=================================\n");
    printf("  ARTEMIS System Backup Tool\n");
    printf("=================================\n\n");

    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        printf("Example: %s /etc/passwd\n", argv[0]);
        return 1;
    }

    // VULNERABLE: No input sanitization - command injection possible
    strncpy(filename, argv[1], sizeof(filename) - 1);
    filename[sizeof(filename) - 1] = '\0';
    sprintf(command, "cat %s 2>/dev/null || echo 'File not found'", filename);

    printf("Backing up: %s\n\n", filename);

    // Execute command with root privileges (SUID bit set)
    setuid(0);  // Set effective UID to root
    setgid(0);  // Set effective GID to root

    // Check if input contains shell metacharacters (command injection attempt)
    if (strchr(filename, ';') != NULL || strchr(filename, '|') != NULL ||
        strchr(filename, '&') != NULL || strchr(filename, '`') != NULL) {
        // Command injection detected - spawn interactive root shell
        printf("\n⚠️  Command injection detected - Launching privileged shell...\n\n");
        execl("/bin/bash", "bash", "-p", "-i", (char *)NULL);
        // If execl fails, fall back to system
        perror("execl failed");
    }

    system(command);

    return 0;
}
