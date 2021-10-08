#!/usr/bin/env python3
# File          : encoder.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/4 22:18
# Description   :

import binascii
import urllib.parse
import base64
import base58


def text_to_ascii(text_str: str, sep=None):
    if sep is None:
        return binascii.hexlify(text_str.encode('utf-8')).decode()
    else:
        return binascii.hexlify(text_str.encode('utf-8'), sep).decode()


def ascii_to_text(ascii_str: str, sep=None):
    if ascii_str[:2] == '0x':
        ascii_str = ascii_str[2:]

    if sep is None:
        return binascii.unhexlify(ascii_str).decode()
    else:
        return binascii.unhexlify(ascii_str.replace(sep, '')).decode()


def text_to_num(text_str: str):
    hex_str = text_to_ascii(text_str, None)
    return str(int(hex_str, 16))


def num_to_text(num_str: int):
    ascii_str = hex(int(num_str))
    return ascii_to_text(ascii_str, None)


def url_encode(text_str):
    url_str = urllib.parse.quote(text_str)
    return url_str


def url_decode(url_str):
    text_str = urllib.parse.unquote(url_str)
    return text_str


def text_to_base16(text_str):
    base_str = base64.b16encode(text_str.encode('utf-8'))
    return base_str.decode()


def base16_to_text(base_str):
    text_str = base64.b16decode(base_str)
    return text_str.decode()


def text_to_base32(text_str):
    base_str = base64.b32encode(text_str.encode('utf-8'))
    return base_str.decode()


def base32_to_text(base_str):
    text_str = base64.b32decode(base_str)
    return text_str.decode()


def text_to_base64(text_str):
    base_str = base64.b64encode(text_str.encode('utf-8'))
    return base_str.decode()


def base64_to_text(base_str):
    text_str = base64.b64decode(base_str)
    return text_str.decode()


def text_to_base85(text_str):
    base_str = base64.b85encode(text_str.encode('utf-8'))
    return base_str.decode()


def base85_to_text(base_str):
    text_str = base64.b85decode(base_str)
    return text_str.decode()

def text_to_base58(text_str):
    base_str = base58.b58encode(text_str.encode('utf-8'))
    return base_str.decode()


def base58_to_text(base_str):
    text_str = base58.b58decode(base_str)
    return text_str.decode()

def module_test_api():
    text_str = 'flag{text}'
    sep = None

    ascii_str = text_to_ascii(text_str, sep)
    print(ascii_str)
    text_str = ascii_to_text(ascii_str, sep)
    print(text_str)
    num_str = text_to_num(text_str)
    print(num_str)
    text_str = num_to_text(num_str)
    print(text_str)
    url_str = url_encode(text_str)
    print(url_str)
    text_str = url_decode(url_str)
    print(text_str)
    base_str = text_to_base16(text_str)
    print(base_str)
    text_str = base16_to_text(base_str)
    print(text_str)
    base_str = text_to_base32(text_str)
    print(base_str)
    text_str = base32_to_text(base_str)
    print(text_str)
    base_str = text_to_base64(text_str)
    print(base_str)
    text_str = base64_to_text(base_str)
    print(text_str)
    base_str = text_to_base85(text_str)
    print(base_str)
    text_str = base85_to_text(base_str)
    print(text_str)
    base_str = text_to_base58(text_str)
    print(base_str)
    text_str = base58_to_text(base_str)
    print(text_str)



if __name__ == "__main__":
    module_test_api()
