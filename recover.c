#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("The file could not be opened\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card

    bool found_jpg = false;
    int counter = 0;
    char filename [8];
    FILE *img = NULL;

    while (fread(buffer, 1 , 512, card) == 512)
    {
        // verificar que los 4 primeros se correspondan con un JPG
        if(buffer [0] == 0xff && buffer [1] == 0xd8 && buffer [2] == 0xff && ((buffer [3] & 0xf0) == 0xe0))
            found_jpg = true;

        if (found_jpg == true)
        {
            if (counter != 0)
            {
                fclose(img);
            }

            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");
            fwrite(buffer, 1 , 512, img);
            found_jpg = false;
            counter ++;
        }
        else if ( counter != 0)
        {
            fwrite(buffer, 1 , 512, img);
        }
    }

fclose(img);
fclose(card);

}
