#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <crypt.h>

int main(int argc, char *argv[]) 
{
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    char newHash[6] = {};
    char guess[6] = {};
    char salt[3];
    salt[0] = argv[1][0];
    salt[1] = argv[1][1];
    char asc[95];
    for (int i = 0; i < 95; i++)  
    {
        asc[i] = (char)(i + 32);
    }
    for (int i = 0; i < 95; i++)
    {
        for (int j = 0; j < 95; j++)
        {
            for (int k = 0; k < 95; k++)
            {
                for (int l = 0; l < 95; l++)
                {
                    for (int m = 0; m < 95; m++)
                    {
                        newHash[0] = asc[i];
                        newHash[1] = asc[j];
                        newHash[2] = asc[k];
                        newHash[3] = asc[l];
                        newHash[4] = asc[m];
                        for (int n = 0, o = 5; n <= 4; n++, o--)
                        {
                            for (int p = 0; p < n + 1; p++)
                            {
                                strncpy(guess, newHash + p, o);
                                guess[o] = '\0';
                                if (strcmp(crypt(guess, salt), argv[1]) == 0)
                                {
                                    printf("%s\n", guess);
                                    return 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

    
        
            
                
                    
             

