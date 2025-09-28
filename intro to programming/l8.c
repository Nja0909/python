#include <stdio.h>

int main() {
    // Part 1: One-Dimensional Array
    int arr[5];
    printf("Enter 5 integers for the 1D array:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("\nThe 1D array elements are:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    // Part 2: Two-Dimensional Array (3x3 matrix)
    int matrix[3][3], sum = 0;
    printf("\n\nEnter elements for the 3x3 matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
            sum += matrix[i][j];
        }
    }

    // Display 2D Array
    printf("\nThe 3x3 matrix is:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    // Display Sum of 2D Array Elements
    printf("\nSum of all elements in the 3x3 matrix = %d\n", sum);

    return 0;
}

