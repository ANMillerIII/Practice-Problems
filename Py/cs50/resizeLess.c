// Resizes a BMP file

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    // remember filenames
    int n = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    // store in width and height to use later for iterating over scanlines, but redefine bi and bf structs with new outfile dimensions
    int inWidth = bi.biWidth;
    int inHeight = bi.biHeight;
    int outWidth = inWidth * n;
    int outHeight = inHeight * n;
    int inPadding = (4 - (inWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int outPadding = (4 - (outWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi.biWidth = outWidth;
    bi.biHeight = outHeight;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * outWidth) + outPadding) * abs(outHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines

    RGBTRIPLE scanline[outWidth * sizeof(RGBTRIPLE)];
    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(inHeight); i < biHeight; i++)
    {
        // iterate over pixels in scanline
        for (int j = 0; j < inWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // stores temporary scanline for vertical size (j * n) + k is the pixel in the scanline array
            for (int k = 0; k < n; k++)
            {
                scanline[(j * n) + k] = triple;
            }
        }

        // skip over padding, if any
        fseek(inptr, inPadding, SEEK_CUR);

        // then add it back (to demonstrate how)
        for (int o = 0; o < n; o++)
        {
            // write scanline o times
            fwrite(scanline, sizeof(RGBTRIPLE), outWidth, outptr);
            // write outPadding, based on new width
            for (int l = 0; l < outPadding; l++)
            {
                fputc(0x00, outptr);

            }
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
