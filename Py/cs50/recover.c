#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // check usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover infile\n");
        return 1;
    }

    // open file containing JPEGs, check if valid
    char *infile = argv[1];
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open file: %s\n", infile);
        return 2;
    }

    // declare buffer array of bytes, initialize image counter, JPEG names, and JPEG file to write to
    uint8_t buffer[512];
    int imageCount = 0;
    char imageName[8];
    FILE *outptr = NULL;

    // loop through entire infile
    while (true)
    {
        // read a 512 byte block of the input file and record size of what was read
        size_t bytesRead = fread(buffer, sizeof(uint8_t), 512, inptr);

        // break out of loop if at end of input file
        if (bytesRead == 0 && feof(inptr))
        {
            break;
        }

        // check if found a JPEG
        bool isJPG = buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;

        // if a JPEG was found but another one is still open for writing, close old one and count it
        if (isJPG && outptr != NULL)
        {
            fclose(outptr);
            imageCount++;
        }

        // if JPEG was found, open and write new JPEG file name
        if (isJPG)
        {
            sprintf(imageName, "%03i.jpg", imageCount);
            outptr = fopen(imageName, "w");
        }

        // write what was read to open JPEG file
        if (outptr != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), bytesRead, outptr);
        }
    }
    // close everything
    fclose(outptr);
    fclose(inptr);

    return 0;
}