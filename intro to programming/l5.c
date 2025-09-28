#include <stdio.h>

int main() {
    int i;

    // Using while loop
    printf("Using while loop:\n");
    i = 1;
    while (i <= 10) {
        printf("%d ", i);
        i++;
    }

    printf("\n\n");

    // Using for loop
    printf("Using for loop:\n");
    for (i = 1; i <= 10; i++) {
        printf("%d ", i);
    }

    printf("\n\n");

    // Using do-while loop
    printf("Using do-while loop:\n");
    i = 1;
    do {
        printf("%d ", i);
        i++;
    } while (i <= 10);

    printf("\n");

    return 0;
}
