#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

int main(int argC, string argV[])
{
    if (argC != 2)
    {
        printf("Missing argument");
        return 1;
    }
    int k = atoi(argV[1]);
    string s = get_string("plaintext: ");
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] >= 65 && s[i] <= 90)
        {
            s[i] = (s[i] + k - 65) % 26 + 65;
        }
        else if (s[i] >= 97 && s[i] <= 122)
        {
            s[i] = (s[i] + k - 97) % 26 + 97;
        }
    }
    printf("ciphertext: %s\n", s);
    return 0;
}
