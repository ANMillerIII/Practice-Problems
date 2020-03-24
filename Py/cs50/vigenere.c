#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int shift(char c)
{
    if (c >= 65 && c <= 90)
    {
        c -= 65;
    }
    else if (c >= 97 && c <= 122)
    {
        c -= 97;
    }
    return c;
}

int main(int argC, string argV[])
{
    if (argC != 2)
    {
        printf("Wrong number of arguments");
        return 1;
    }
    for (int j = 0; j < strlen(argV[1]); j++)
    {
        if (!isalpha(argV[1][j]))
        {
            printf("Usage: ./vignere keyword");
            return 1;
        }
    }
    string k = argV[1];
    int kLength = strlen(k);
    string s = get_string("plaintext: ");
    int sLength = strlen(s);
    for (int i = 0, j = 0; i <= strlen(s); i++)
    {
        k[j] = shift(k[j % kLength]);
        if (s[i] >= 65 && s[i] <= 90)
        {
            s[i] = (s[i] + k[j] - 65) % 26 + 65;
            j++;
        }
        else if (s[i] >= 97 && s[i] <= 122)
        {
            s[i] = (s[i] + k[j] - 97) % 26 + 97;
            printf("%i\n", s[i]);
            j++;
        }
        else
        {
            s[i] = s[i];
        }
    }
    printf("ciphertext: %s\n", s);
    return 0;
}

