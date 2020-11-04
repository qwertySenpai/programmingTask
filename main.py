# -------------------------------------------------------------------------------------------------------------------
# Author: github@qwertySenpai
# GitHub: https://github.com/qwertySenpai
# Creating Date: 04.11.2020
# Tested with Python 3.7
# -------------------------------------------------------------------------------------------------------------------
# PROGRAMMING TASK
# -------------------------------------------------------------------------------------------------------------------
# For purpose of this task, you will find two functions:
#
# Fibonacci Calculation:
# This function calculates 'n-th' fibonacci of given number 'n' as parameter. It will check if the input is
# an positive integer. For calculation a recursive function is used.
#
# Excluding Repeating Words:
# This function will give an output of given words as prompt input excluding repeating words.
# First, the user is asked to input an integer greater than 0 for number of expecting inputs (otherwise it will
# give a warning text).
# Second, the user is asked to input any word (only alphabetical characters are allowed!).
# Third, the word will be appended into a list if not already existing.
# Finally, the word list will be printed as an output.
# -------------------------------------------------------------------------------------------------------------------


def fibonacci(n):
    if isinstance(n, int) and n >= 0:   # check if 'n' is an integer and positive number
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("Sadece positif sayilar kabul edilmektedir. '0' geri verildi...")
        return 0


def exclude_repeating_words():

    words = []

    while True:
        number_of_words = input("Kac Kelime Gireceksiniz: ")

        if number_of_words.isdecimal():
            number_of_words = int(number_of_words)

            if number_of_words < 1:
                print("Sadece sifirdan yüksek sayi kabul edilmektedir. Lütfen tekrar giriniz.\n")
            else:
                break
        else:
            print("Sadece sifirdan yüksek sayi kabul edilmektedir. Lütfen tekrar giriniz.\n")

    for i in range(number_of_words):
        while True:
            input_word = input("Kelime giriniz: ")

            if input_word.isalpha():    # check if only alphabetic characters
                break
            else:
                print("Sadece harfden olusan kelime kabul edilmektedir. Lütfen tekrar giriniz.\n")

        if input_word not in words:
            words.append(input_word)

    print("\nEssiz Kelimeler: " + ", ".join(words))
