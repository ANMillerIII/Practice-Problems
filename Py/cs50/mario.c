#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size = 0;
    do
    {
        size = get_int("Size? ");
    } 
    while (size < 1 || size > 8);
    for (int i = 1; i <= size; i++)
    {
        for (int j = 0; j < size - i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int z = 0; z < i; z++)
        {
            printf("#");
        }
        printf("\n");
    }
}
