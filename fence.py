#!/usr/bin/env python3
# File          : fence.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/8 20:27
# Description   :

def fence_encode(plaintext, key: int):
    ciphertext = ""
    for i in range(key):
        for j in range(i, len(plaintext), key):
            ciphertext += plaintext[j]

    return ciphertext


def fence_decode(ciphertext, key: int):
    plaintext = [""] * len(ciphertext)
    index = 0
    for i in range(key):
        for j in range(i, len(ciphertext), key):
            plaintext[j] = ciphertext[index]
            index += 1

    return "".join(plaintext)


def blasting(ciphertext, output_file, len_range=None):
    if len_range is None:
        key_range = list(range(2, len(ciphertext)//2+1))

    f = open(output_file, 'a')

    for key in key_range:
        plaintext = fence_decode(ciphertext, key)
        if plaintext[:5] == 'flag{' and plaintext[-1] == "}":
            print("key is {}.".format(key))
            print("plaintext is {}.".format(plaintext))
            f.write(str(key) + "\t" + plaintext + "\n")

    f.close()


def module_test_api():
    plaintext = "flag{zhalan_mima_hahah}"
    key = 4
    ciphertext = fence_encode(plaintext, key)
    print(ciphertext)
    plaintext = fence_decode(ciphertext, key)
    print(plaintext)

    output_file = "./output_plaintext/fence_blasting_plaintext.txt"
    blasting(ciphertext, output_file)


if __name__ == "__main__":
    module_test_api()
