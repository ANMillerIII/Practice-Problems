#include <cs50.h>
#include <stdio.h>
#include <math.h>

float get_amount(void);

int main(void)
{
    int count = 0;
    int change = 0;
    float dollars = get_amount();
    int cents = round(dollars * 100);
    printf("Change owed: %i\n", cents);
    while (change < cents - 24 && change % 25 >= 0)
    {
        change = change + 25;
        count = count + 1;  
    }    
    while (change < cents - 9 && change % 10 >= 0)
    {
        change = change + 10;
        count = count + 1;  
    }    
    while (change < cents - 4 && change % 5 >= 0)
    {
        change = change + 5;
        count = count + 1;  
    }  
    while (change < cents && change % 1 >= 0)
    {
        change = change + 1;
        count = count + 1;  
    }    
    printf("%i", count);
}

float get_amount(void)
{
    float amount;
    do
    {
        amount = get_float("Amount tendered ($)?");
    }
    while (amount < 0);
    return amount;
    printf("\n");
}
