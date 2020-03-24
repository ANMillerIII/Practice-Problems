#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <crypt.h>
#include <unistd.h>

int main(int argc, char* argv[]) 
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
    char arr[95];
    for(int i = 0; i < 95; i++) arr[i] = (char) (i + 32);
    {
        for(int i = 0; i < 95; i++)
        {
            for(int j = 0; j < 95; j++)
            {
                for(int k = 0; k < 95; k++)
                {
                    for(int l = 0; l < 95; l++)
                    {
                        for(int m = 0; m < 95; m++)
                        {
                            newHash[0] = arr[i];
                            newHash[1] = arr[j];
                            newHash[2] = arr[k];
                            newHash[3] = arr[l];
                            newHash[4] = arr[m];
                            for(int q = 0, r = 5; q <= 4; q++, r--)
                            {
                                for(int s = 0; s < q + 1; s++) 
                                {
                                    strncpy(guess, newHash+s, r);
                                    guess[r] = '\0';
                                    if(strcmp(crypt(guess, salt), argv[1]) == 0) 
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
}
    
        
            
                
                    
             

