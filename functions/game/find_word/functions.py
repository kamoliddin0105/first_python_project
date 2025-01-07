import random

from words import words


def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += '_'
    return display_letter


def play():
    word = get_word()
    word_letters = set(word)  # Unique letters in the word
    user_letters = ""  # Letters guessed by the user
    print(f"Men {len(word)} xonali so'z o'yladim. Uni topa olasizmi?")

    while len(word_letters) > 0:
        print(display(user_letters, word))  # Display the word with guessed letters

        if len(user_letters) > 0:
            print(f"Shu paytgacha kiritgan harflaringiz: {user_letters}")

        letter = input("Harf kiriting: ").upper()

        # Validate input
        if len(letter) != 1 or not letter.isalpha():
            print("Iltimos, faqat bitta harf kiriting!")
            continue

        if letter in user_letters:
            print("Bu harfni oldin kiritgansiz.")
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri!")
        else:
            print(f"{letter} harfi noto'g'ri.")
        user_letters += letter

        if len(word_letters) == 0:
            break

    print(f"Tabriklayman! Siz '{word}' so'zini {len(user_letters)} ta urinishda topdingiz!")

