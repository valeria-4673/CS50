#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in argv[1] is a digit
    string s = argv[1];

    bool input_check = only_digits(s);
    if (input_check == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert argv[1] from a `string` to an `int`

    int key = atoi(argv[1]);
    printf("la key numerica es: %i\n", key);

    // Prompt user for plaintext

    string plaintext = get_string("plaintext: ");

    // For each character in the plaintext:
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        if (isalpha(plaintext[i]) && (isupper(plaintext[i])))
            printf("%c", ((plaintext[i] - 65 + key) % 26 + 65));
        else if (isalpha(plaintext[i]) && islower(plaintext[i]))
            printf("%c", ((plaintext[i] - 97 + key) % 26 + 97));
        else
            printf("%c", plaintext[i]);
    }
    printf("\n");

    return 0;
}

bool only_digits(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isdigit(s[i]))
            return true;
        else
            return false;
    }

    return 0;
}
