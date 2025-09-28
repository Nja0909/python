#include <stdio.h>

int main() {
    int i;

    // Using break: Stop printing when number reaches 5
    printf("Using break (Stop at 5):\n");
    for (i = 1; i <= 10; i++) {
        if (i == 5) {
            break; // Exit loop when i is 5
        }
        printf("%d ", i);
    }

    printf("\n\n");

    // Using continue: Skip printing number 3
    printf("Using continue (Skip 3):\n");
    for (i = 1; i <= 10; i++) {
        if (i == 3) {
            continue; // Skip current iteration when i is 3
        }
        printf("%d ", i);
    }

    printf("\n");

    return 0;
}
