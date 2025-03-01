from cs50 import get_string

def count_letters(text):
    count_letters = 0
    for letra in text:
        if (letra.isalpha()):
            count_letters += 1
    return count_letters

def count_words(text):
    count_words = 1
    for palabra in text:
        if (palabra == " "):
            count_words += 1
    return count_words

def count_sentences(text):
    count_sentences = 0
    for i in text:
        if (i == "." or i == "!" or i == "?"):
            count_sentences += 1
    return count_sentences

def main():
    text = get_string("Text: ")

    letters = count_letters(text)

    words = count_words(text)

    sentences = count_sentences(text)

    l = (letters / words) * 100
    s = (sentences / words) * 100
    index = 0.0588 * l - 0.296 * s - 15.8

    if (index >= 16):
        print("Grade 16+")
    elif (index < 1):
        print("Before Grade 1")
    else:
        print ("Grade ", round(index))
main()
