#!/usr/bin/env python3
# File          : atbash.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/8 23:29
# Description   :

def atbash_encode(plaintext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_map = alphabet[::-1] + alphabet.lower()[::-1]
    alphabet += alphabet.lower()
    ciphertext = ""
    for i in plaintext:
        index = alphabet.find(i)
        if index != -1:
            ciphertext += alphabet_map[index]
        else:
            ciphertext += i

    return ciphertext


def module_test_api():
    p = "flag{ok_atbash_flag}"
    c = atbash_encode(p)
    print(c)
    p = atbash_encode(c)
    print(p)

if __name__ == "__main__":
    module_test_api()