#!/usr/bin/env python3
# File          : hill.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/14 21:33
# Description   :

import numpy as np


def hill_encrypt(plaintext, key):
    n, m = key.shape
    if n != m:
        print("[Error] Error key!")
        return ''
    plaintext = plaintext.upper()
    index_lst = []
    num_lst = []
    for i in range(len(plaintext)):
        index_lst.append(ord(plaintext[i]) - ord('A'))
        if (i + 1) % 3 == 0:
            num_lst.append(index_lst)
            index_lst = []
    mat_m = [np.matrix(i).T for i in num_lst]
    mat_c = [key * i % 26 for i in mat_m]

    num_c_lst = []
    for i in mat_c:
        for j in range(len(key)):
            num_c_lst.append(i.tolist()[j][0])
    ciphertext = ''.join([chr(x + ord('A')) for x in num_c_lst])

    return ciphertext


def module_test_api():
    plaintext = 'actdaa'
    key = "[[6, 24, 1], [13, 16, 10], [20, 17, 15]]"
    key = eval(key)
    key = np.matrix(key)
    ciphertext = hill_encrypt(plaintext, key)
    print(ciphertext)


if __name__ == "__main__":
    module_test_api()
