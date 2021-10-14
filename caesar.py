#!/usr/bin/env python3
# File          : caesar.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/8 21:18
# Description   :

def caesar_encrypt(plaintext, key):
    key = int(key)
    ciphertext = ""
    for i in plaintext:
        ciphertext += chr((ord(i) + key) % 128)
    return ciphertext


def caesar_decrypt(ciphertext, key):
    key = int(key)
    plaintext = ""
    for i in ciphertext:
        # print(i, ord(i), ord(i)-key, chr((ord(i)-key) % 128))
        plaintext += chr((ord(i) - key) % 128)
    return plaintext


def caesar_brute(ciphertext):
    for key in range(128):
        plaintext = caesar_decrypt(ciphertext, key + 1)
        if "flag" in plaintext:
            print("key is {}".format(key + 1))
            print("plaintext is {}.".format(plaintext))


def rot13(ciphertext):
    plaintext = ""
    for i in ciphertext:
        if ord(i) in range(ord('A'), ord('Z') + 1):
            plaintext += chr((ord(i) + 13 - ord('A')) % 26 + ord('A'))
        elif ord(i) in range(ord('a'), ord('z') + 1):
            plaintext += chr((ord(i) + 13 - ord('a')) % 26 + ord('a'))
        else:
            plaintext += i
    return plaintext


def alphabet_caesar_encrypt(ciphertext, key):
    key = int(key)
    plaintext = ""
    for i in ciphertext:
        if ord(i) in range(ord('A'), ord('Z') + 1):
            plaintext += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
        elif ord(i) in range(ord('a'), ord('z') + 1):
            plaintext += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
        else:
            plaintext += i
    return plaintext


def alphabet_caesar_decrypt(plaintext, key):
    key = int(key)
    ciphertext = ""
    for i in plaintext:
        if ord(i) in range(ord('A'), ord('Z') + 1):
            ciphertext += chr((ord(i) - key - ord('A')) % 26 + ord('A'))
        elif ord(i) in range(ord('a'), ord('z') + 1):
            ciphertext += chr((ord(i) - key - ord('a')) % 26 + ord('a'))
        else:
            ciphertext += i
    return ciphertext


def module_test_api():
    ciphertext = "39.4H/?BA2,0.2@.?J"
    caesar_brute(ciphertext)
    c = "iodj~ndlvdplpd\x00"
    k = 3
    m = caesar_decrypt(c, k)
    print(m)
    c = "iodj{ndlvdplpd}"
    m = alphabet_caesar_decrypt(c, k)
    print(m)
    c = alphabet_caesar_encrypt(m, k)
    print(c)


if __name__ == "__main__":
    module_test_api()
