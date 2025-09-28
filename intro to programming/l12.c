#include <stdio.h>

int main() {
    FILE *fp;
    char str[100];

    // Step 1: Create a file and write a string into it
    fp = fopen("example.txt", "w");  // Open file in write mode
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    printf("Enter a string to write into the file: ");
    fgets(str, sizeof(str), stdin);

    fprintf(fp, "%s", str);  // Write string to file
    fclose(fp);  // Close the file after writing

    printf("\nData written to file successfully.\n");

    // Step 2: Open the file again to read and display its contents
    fp = fopen("example.txt", "r");  // Open file in read mode
    if (fp == NULL) {
        printf("Error opening file for reading!\n");
        return 1;
    }

    printf("\nReading data from file:\n");

    while (fgets(str, sizeof(str), fp) != NULL) {
        printf("%s", str);  // Display content
    }

    fclose(fp);  // Close the file after reading

    return 0;
}
