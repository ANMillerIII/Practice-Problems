// Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    int length = argv[1];
    int arr[] = {};
    for (int i = 0; i < argv[1]; i++)
    {
        int arr[i] = atio(argv[1][i])
    }
    for (int j = 0,  j < length; j++, k++, l++)
    {
        for (int k = 0; k < length; k++)
        {
            for (int l = 0; l < length; l++)
            {
                if (arr[j]**2 + arr[k]**2 == arr[l]**2)
                {
                    return true;
                }
            }
        }
    }
    return false;
}








// get array of integers
 check if all are integers?
// for every set of int in the array
// for (int i = 0; j = 0; k = 0; i < array length; i++, j++, k++)
    // check if int i^2 +int j^2 = int k^2;
        // return true if so
    // return false if not

