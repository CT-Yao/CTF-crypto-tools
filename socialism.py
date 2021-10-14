#!/usr/bin/env python3
# File          : socialism.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/10 0:07
# Description   :

import random

key_lst = ['富强', '民主', '文明', '和谐',
           '自由', '平等', '公正', '法治',
           '爱国', '敬业', '诚信', '友善']


def socialism_encode(plaintext):
    ciphertext = ""

    letters = [x for x in plaintext.encode('utf8')]

    for letter in letters:
        letter_lst = [int(x, 16) for x in "{:0>2}".format(hex(letter)[2:])]
        n_lst = []
        for n in letter_lst:
            if n < 10:
                n_lst.append(n)
            else:
                if random.uniform(0, 1) > 0.5:
                    n_lst.append(10)
                    n_lst.append(n - 10)
                else:
                    n_lst.append(11)
                    n_lst.append(n - 6)
        ciphertext += ''.join([key_lst[x] for x in n_lst])

    return ciphertext


def socialism_decode(ciphertext):
    n_lst = [key_lst.index(ciphertext[x:x + 2]) for x in range(0, len(ciphertext), 2)]
    hex_lst = []
    i = 0
    while i < len(n_lst):
        if n_lst[i] < 10:
            hex_lst.append(n_lst[i])
        else:
            if n_lst[i] == 10:
                hex_lst.append(sum(n_lst[i:i + 2]))
            elif n_lst[i] == 11:
                hex_lst.append(n_lst[i + 1] + 6)
            else:
                print("[Error]")
            i += 1
        i += 1
    hex_lst = [hex(x)[2:] for x in hex_lst]
    new_hex_lst = [int("".join(hex_lst[x:x + 2]), 16) for x in range(0, len(hex_lst), 2)]
    plaintext = bytes(new_hex_lst).decode()

    return plaintext


def module_test_api():
    c = '比赛'
    m = socialism_encode(c)
    print(m)
    c = socialism_decode(m)
    print(c)


if __name__ == "__main__":
    module_test_api()
