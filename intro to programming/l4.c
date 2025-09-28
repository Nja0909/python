#include <stdio.h>

int main() {
    int num, month;

    // Part 1: Even or Odd using if-else
    printf("Enter a number to check if it's even or odd: ");
    scanf("%d", &num);

    if (num % 2 == 0) {
        printf("%d is Even\n", num);
    } else {
        printf("%d is Odd\n", num);
    }

    // Part 2: Display month using switch
    printf("\nEnter a number (1-12) to get the month name: ");
    scanf("%d", &month);

    printf("Month: ");
    switch(month) {
        case 1:  printf("January"); break;
        case 2:  printf("February"); break;
        case 3:  printf("March"); break;
        case 4:  printf("April"); break;
        case 5:  printf("May"); break;
        case 6:  printf("June"); break;
        case 7:  printf("July"); break;
        case 8:  printf("August"); break;
        case 9:  printf("September"); break;
        case 10: printf("October"); break;
        case 11: printf("November"); break;
        case 12: printf("December"); break;
        default: printf("Invalid month number (must be 1–12)");
    }

    return 0;
}
