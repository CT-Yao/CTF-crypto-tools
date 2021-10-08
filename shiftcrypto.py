#!/usr/bin/env python3
# File          : shiftcrypto.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/7 21:55
# Description   :

import itertools
from concurrent.futures import ThreadPoolExecutor


def shift_encrypt(plaintext, key):
    l = len(key)
    ciphertext = ""
    for i in range(0, len(plaintext), l):
        new_block = [""] * l
        if i + 1 > len(plaintext):
            block = plaintext[i:]
        else:
            block = plaintext[i:i + l]
        for j in range(len(block)):
            new_block[int(key[j]) - 1] = block[j]
        ciphertext += "".join(new_block)

    return ciphertext


def shift_decrypt(ciphertext, key):
    l = len(key)
    plaintext = ""
    for i in range(0, len(ciphertext), l):
        new_block = [""] * l
        if i + l > len(ciphertext):
            block = ciphertext[i:]
            index_map = [int(key[x]) - 1 for x in range(len(block))]
            index_map.sort()
            for j in range(len(block)):
                new_block[j] = block[index_map.index(int(key[j]) - 1)]
        else:
            block = ciphertext[i:i + l]
            for j in range(len(block)):
                new_block[j] = block[int(key[j]) - 1]
        plaintext += "".join(new_block)
    return plaintext


def blasting_task(ciphertext, key, f):
    plaintext = shift_decrypt(ciphertext, key)
    if plaintext[:5] == 'flag{' and plaintext[-1] == '}':
        print("key is {}.".format(key))
        print("plaintext is {}".format(plaintext))
        f.write(key + "\t" + plaintext + "\n")


def shift_brute(ciphertext, output_file, len_range=None):
    if len_range is None:
        len_range = list(range(2, min(len(ciphertext)), 9))

    f = open(output_file, 'a+')
    pool = ThreadPoolExecutor(max_workers=48)
    for key_len in len_range:
        for key in itertools.permutations("".join([str(i + 1) for i in range(key_len)]), key_len):
            pool.submit(blasting_task, ciphertext, ''.join(key), f)
    f.close()


def module_test_api():
    plaintext = "flag{easy_easy_crypto}"
    key = "3124"
    ciphertext = shift_encrypt(plaintext, key)
    print(ciphertext)
    plaintext = shift_decrypt(ciphertext, key)
    print(plaintext)

    output_file = './output_plaintext/shift_blasting_plaintext.txt'
    shift_brute(ciphertext, output_file, len_range=list(range(2,9)))

if __name__ == "__main__":
    module_test_api()