#include <stdio.h>

int main() {
    int a, b;

    // Input two integers
    printf("Enter first integer: ");
    scanf("%d", &a);

    printf("Enter second integer: ");
    scanf("%d", &b);

    // Arithmetic Operations
    printf("\n--- Arithmetic Operations ---\n");
    printf("Addition: %d + %d = %d\n", a, b, a + b);
    printf("Subtraction: %d - %d = %d\n", a, b, a - b);
    printf("Multiplication: %d * %d = %d\n", a, b, a * b);

    if (b != 0) { // Avoid division by zero
        printf("Division: %d / %d = %d\n", a, b, a / b);
        printf("Modulus: %d %% %d = %d\n", a, b, a % b);
    } else {
        printf("Division and modulus by zero is not allowed.\n");
    }

    // Relational Operations
    printf("\n--- Relational Operations ---\n");
    printf("%d == %d: %d\n", a, b, a == b);
    printf("%d != %d: %d\n", a, b, a != b);
    printf("%d > %d: %d\n", a, b, a > b);
    printf("%d < %d: %d\n", a, b, a < b);
    printf("%d >= %d: %d\n", a, b, a >= b);
    printf("%d <= %d: %d\n", a, b, a <= b);

    // Logical Operations
    printf("\n--- Logical Operations ---\n");
    printf("%d && %d = %d\n", a, b, a && b);  // Logical AND
    printf("%d || %d = %d\n", a, b, a || b);  // Logical OR
    printf("!%d = %d\n", a, !a);              // Logical NOT for a
    printf("!%d = %d\n", b, !b);              // Logical NOT for b

    return 0;
}
