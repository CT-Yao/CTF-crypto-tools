#!/usr/bin/env python3
# File          : affine.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/10 19:26
# Description   :

alphabet = "abcdefghijklmnopqrstuvwxyz"


def gcd(a, b):
    while b != 0:
        m = a % b
        a = b
        b = m
    return a


def modinv(a, b):
    n = 1
    while (a * n) % b != 1:
        n += 1
    return n


def affine_encode(plaintext, a, b, alphabet=alphabet):
    plaintext = plaintext.lower()

    ciphertext = ""
    for letter in plaintext:
        if alphabet.index(letter) != -1:
            ciphertext += alphabet[(a * alphabet.index(letter) + b) % len(alphabet)]
        else:
            ciphertext += letter
    return ciphertext


def affine_decode(ciphertext, a, b, alphabet=alphabet):
    ciphertext = ciphertext.lower()
    plaintext = ""

    for letter in ciphertext:
        if alphabet.index(letter) != -1:
            plaintext += alphabet[(modinv(a, len(alphabet)) * (alphabet.index(letter) -b)) % len(alphabet)]
        else:
            plaintext += letter

    return plaintext


def module_test_api():
    plaintext = "affinecipher"
    a = 5
    b = 8
    ciphertext = affine_encode(plaintext, a, b)
    print(ciphertext)
    plaintext = affine_decode(ciphertext, a, b)
    print(plaintext)


if __name__ == "__main__":
    module_test_api()
