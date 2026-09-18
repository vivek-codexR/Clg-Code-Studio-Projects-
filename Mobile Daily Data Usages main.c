#include <stdio.h>
int main() {
    float data, total = 0;
    int count = 0;
    for(int i = 1; i <= 7; i++) {
        printf("Enter data for day %d: ", i);
        scanf("%f", &data);
        total = total + data;
        if(data > 2) {
            count = count + 1;
        }
    }
    printf("\nTotal = %f GB", total);
    printf("\nDays above 2 GB = %d", count);
    return 0;
}
