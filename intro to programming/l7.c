#include <stdio.h>

// Function Declaration
int factorial(int n);

int main() {
    int num, result;

    // Input a number from the user
    printf("Enter a positive integer: ");
    scanf("%d", &num);

    // Function Call
    result = factorial(num);

    // Display the result
    printf("Factorial of %d is %d\n", num, result);

    return 0;
}

// Function Definition
int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}
