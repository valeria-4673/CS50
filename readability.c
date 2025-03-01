#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Print the grade level
    if (index < 1)
        printf("Before Grade 1\n");
    else if (index >= 16)
        printf("Grade 16+\n");
    else
        printf("Grade %i\n", (int) round(index));
}

// Return the number of letters in text

int count_letters(string text)
{
    int letter_counter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
            letter_counter += 1;
    }
    return letter_counter;
}

// Return the number of words in text

int count_words(string text)
{
    int words_counter = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isblank(text[i]))
            words_counter += 1;
    }
    return words_counter;
}

// Return the number of sentences in text

int count_sentences(string text)
{
    int sentences_counter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            sentences_counter += 1;
    }
    return sentences_counter;
}
