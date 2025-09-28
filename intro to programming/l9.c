#include <stdio.h>

int main() {
    int num = 10;       // Declare an integer variable
    int *ptr;           // Declare a pointer to an integer

    ptr = &num;         // Store address of num in ptr

    printf("Original value of num: %d\n", num);
    printf("Address of num: %p\n", &num);
    printf("Value stored in ptr (address of num): %p\n", ptr);
    printf("Value pointed to by ptr: %d\n", *ptr);

    // Modify the value of num using pointer
    *ptr = 25;

    printf("\nAfter modifying value using pointer:\n");
    printf("New value of num: %d\n", num);

    return 0;
}
