#!/usr/bin/env python3
# File          : bacon.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/9 13:51
# Description   :

import re


# alphabet = {"A": "aaaaa", "B": "aaaab", "C": "aaaba", "D": "aaabb", "E": "aabaa", "F": "aabab", "G": "aabba",
# "H": "aabbb", "I": "abaaa", "J": "abaab", "K": "ababa", "L": "ababb", "M": "abbaa", "N": "abbab",
# "O": "abbba", "P": "abbbb", "Q": "baaaa", "R": "baaab", ""}


def bacon_encode(plaintext):
    plaintext = plaintext.upper()

    ciphertext = ""
    for i in plaintext:
        if re.match("[A-Z]", i):
            index = ord(i) - ord('A')
            bin_str = "{:0>5}".format(bin(index)[2:])
            bacon_str = bin_str.replace('0', 'A').replace('1', 'B')
            ciphertext += bacon_str
        else:
            ciphertext += i

    return ciphertext


def bacon_decode(ciphertext):
    ciphertext = ciphertext.upper()

    plaintext = ""
    index = 0
    while index < len(ciphertext):
        letter = ciphertext[index:index + 5]
        if all([1 if x in 'AB' else 0 for x in letter]):
            index += 5
            plaintext += chr(int(letter.replace('A', '0').replace('B', '1'), 2) + ord('A'))
        else:
            plaintext += ciphertext[index]
            index += 1
    return plaintext


c = "flag{bacon}"
m = bacon_encode(c)
print(m)
c = bacon_decode(m)
print(c)
