#include <stdio.h>

// Define structure
struct Student {
    char name[50];
    int roll;
    float marks;
};

int main() {
    struct Student students[3];  // Array of 3 students

    // Input student details
    printf("Enter details of 3 students:\n");
    for (int i = 0; i < 3; i++) {
        printf("\nStudent %d:\n", i + 1);
        printf("Name: ");
        scanf(" %[^\n]", students[i].name);  // Read string with spaces
        printf("Roll Number: ");
        scanf("%d", &students[i].roll);
        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }

    // Display student details
    printf("\n--- Student Details ---\n");
    for (int i = 0; i < 3; i++) {
        printf("\nStudent %d:\n", i + 1);
        printf("Name: %s\n", students[i].name);
        printf("Roll Number: %d\n", students[i].roll);
        printf("Marks: %.2f\n", students[i].marks);
    }

    return 0;
}
