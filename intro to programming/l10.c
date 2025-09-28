#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];

    // Input two strings from the user
    printf("Enter the first string: ");
    fgets(str1, sizeof(str1), stdin);

    // Remove newline character if present
    str1[strcspn(str1, "\n")] = '\0';

    printf("Enter the second string: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = '\0';

    // Concatenate str2 to str1
    strcat(str1, str2);

    // Display concatenated string
    printf("\nConcatenated String: %s\n", str1);

    // Display length of concatenated string
    printf("Length of concatenated string: %lu\n", strlen(str1));

    return 0;
}
