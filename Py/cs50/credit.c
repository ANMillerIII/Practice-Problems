#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

bool digits(char *ccString);
    
int main(void)
{
    char *ccString = get_string("Number: ");
    int ccLen = strlen(ccString);
    int l = 0;
    while (!digits(ccString) || ccLen == 0)
    {
        ccString = get_string("Number: ");
        ccLen = strlen(ccString);
    }
    int ccNum[ccLen];
    for (int i = 0; i < ccLen; i++)
    {
        ccNum[i] = ccString[i] - 48;
    }
    int ccLuhn[ccLen];;
    int sumLuhn = 0;
    for (int j = ccLen - 2; j >= 0; j -= 2)
    {
        ccLuhn[j] = 2 * ccNum[j] / 10 + 2 * ccNum[j] % 10;
        sumLuhn += ccLuhn[j];
        
    }
    for (int k = ccLen - 1; k >= 0; k -= 2)
    {
        sumLuhn += ccNum[k];
    }
    if (sumLuhn % 10 != 0 || ccLen < 13)
    {
        printf("INVALID\n");
        return 0;
    }
    if (ccLen == 15 && ccNum[0] == 3 && (ccNum[1] == 4 || ccNum[1] == 7))
    {
        printf("AMEX\n");
    }
    else if (ccLen == 16 && ccNum[0] == 5 && (ccNum[1] >= 1 && ccNum[1] <= 5))
    {
        printf("MASTERCARD\n");
    }
    else if ((ccLen >= 13 && ccLen <= 16) && ccNum[0] == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

bool digits(char *ccString)
{
    for (int w = 0; w < strlen(ccString); w++)
    {
        if (!isdigit(ccString[w]))
        {
            return false;
        }
    }
    return true;
}
