#!/usr/bin/env python3
# File          : morse.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/4 11:41
# Description   : 

alphabet_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..',
                     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                     '8': '---..', '9': '----.', '0': '-----',
                     ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.', '?': '..--..', '/': '-..-.',
                     '-': '-....-', '_': '..--.-', '(': '-.--.', ')': '-.--.-', "'": '.----.', '+': '.-.-.',
                     '=': '-...-', '@': '.--.-.', ' ': ' ', '': ''}

morse_to_alphabet = {v: k for k, v in alphabet_to_morse.items()}


def _move_unusable_char(raw_string):
    return ''.join(list(filter(lambda char: char in alphabet_to_morse, raw_string.upper())))


def morse_encode(text_string):
    morse_string = []
    string = _move_unusable_char(text_string)
    string = string.upper()
    words = string.split(' ')
    for word in words:
        morse_letters = []
        for letter in word:
            morse_letters.append(alphabet_to_morse[letter])
        morse_word = '/'.join(morse_letters)
        morse_string.append(morse_word)
    return " ".join(morse_string)


def morse_decode(morse_string):
    text_string = []
    morse_words = morse_string.split(' ')
    for morse_word in morse_words:
        letters = []
        morse_letters = morse_word.split('/')
        for morse_letter in morse_letters:
            letters.append(morse_to_alphabet[morse_letter])
        word = ''.join(letters)
        text_string.append(word)
    return " ".join(text_string)


morse_code = morse_encode('FLAG MORSE ^')
print(morse_code)
text = morse_decode(morse_code)
print(text)
