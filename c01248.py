#!/usr/bin/env python3
# File          : c01248.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/8 20:01
# Description   :

def c01248_decode(ciphertext):
    ciphertext = ciphertext.strip()
    letters = ciphertext.split('0')
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for each in letters:
        index = sum([int(x) for x in each])
        if index < 1 or index > 26:
            print("[Error] number out of alphabet range.")
            return None
        plaintext += alphabet[index - 1]
    return plaintext


def c01248_encode(plaintext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = plaintext.strip()
    letters_to_num = []
    for letter in plaintext:
        if letter not in alphabet:
            print("[Error] letter of plaintext out of range.")
            return None
        letters_to_num.append(alphabet.index(letter) + 1)

    ciphertext = ""
    for num in letters_to_num:
        if num >= 8:
            ciphertext += int(num / 8) * "8"
        if num % 8 >= 4:
            ciphertext += int(num % 8 / 4) * "4"
        if num % 4 >= 2:
            ciphertext += int(num % 4 / 2) * "2"
        if num % 2 >= 1:
            ciphertext += int(num % 2 / 1) * "1"
        ciphertext += "0"

    return ciphertext[:-1]


def module_test_api():
    # ciphertext is not unique.
    ciphertext = "8842101220480224404014224202480122"
    plaintext = c01248_decode(ciphertext)
    print(plaintext)
    ciphertext = c01248_encode(plaintext)
    print(ciphertext)


if __name__ == "__main__":
    module_test_api()
