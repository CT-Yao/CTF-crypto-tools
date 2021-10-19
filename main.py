#!/usr/bin/env python3
# File          : main.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/4 16:40
# Description   : crypto tools entry.


import getopt
import sys

import atbash
import c01248
import caesar
import encoder
import morse


def usage():
    usage_doc = """
        -------------------------------------------------------------
        |           Python Encoder v1.0                             |
        -------------------------------------------------------------     
        | Usage: python3 main.py -options [input]                   |
        |   * -i: input string.                                     |
        |   * -m: encode or decode method.                          |
        |   * -s: separator, only one char('-', ',', ' ' and so on) |
        | Encoder method:                                           |
        |   * t2ascii, ascii2t: text <-> ascii                      |
        |   * t2num, num2t: text <-> int num                        |
        |   * t2morse, morse2t: text <-> morse code                 |
        |   * t2url, url2t: text <-> url encode                     |
        |   * t2b(num), b(num)2t: text <-> base(num)                | 
        -------------------------------------------------------------     
    """
    print(usage_doc)


input_text = None
encode_mode = None
separator = None
key = None

encoder_dict = {'t2num': encoder.text_to_num,
                'num2t': encoder.num_to_text,

                't2b16': encoder.text_to_base16,
                't2b32': encoder.text_to_base32,
                't2b64': encoder.text_to_base64,
                't2b85': encoder.text_to_base85,

                'b162t': encoder.base16_to_text,
                'b322t': encoder.base32_to_text,
                'b642t': encoder.base64_to_text,
                'b852t': encoder.base85_to_text,

                't2morse': morse.morse_encode,
                'morse2t': morse.morse_decode,

                't2atbash': atbash.atbash_encode,
                'atbash2t': atbash.atbash_encode,

                't2c01248': c01248.c01248_encode,
                'c012482t': c01248.c01248_decode,

                'rot13': caesar.rot13,

                'caeserbrute': caesar.caesar_brute,
                }

encoder_sep_dict = {'t2ascii': encoder.text_to_ascii,
                    'ascii2t': encoder.ascii_to_text}

encoder_key_dict = {'t2caeser': caesar.caesar_encrypt,
                    'caeser2t': caesar.caesar_decrypt,
                    't2a-caeser': caesar.alphabet_caesar_encrypt,
                    'a-caeser2t': caesar.alphabet_caesar_decrypt}

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:m:s:k:', ['help', 'input', 'mode', 'sep', 'key'])
except getopt.GetoptError as e:
    opts = None
    print('[Error] Options error! {}'.format(e))
    usage()
    exit()

for o, a in opts:
    if o in ('-h', '--help'):
        usage()
        exit()
    elif o in ('-i', '--input'):
        input_text = a
    elif o in ('-m', '--mode'):
        encode_mode = a
    elif o in ('-s', '--sep'):
        separator = a
    elif o in ('-k', '--key'):
        key = a

if input_text is None or input_text == '':
    print("[Error] Please input text!")
    exit()
elif separator is not None and len(separator) != 1:
    print("[Error] Separator only one char!")
    exit()

res = None
try:
    if encode_mode in encoder_dict:
        res = encoder_dict[encode_mode](input_text)
    elif encode_mode in encoder_sep_dict:
        res = encoder_sep_dict[encode_mode](input_text, separator)
    elif encode_mode in encoder_key_dict:
        res = encoder_key_dict[encode_mode](input_text, key)
    else:
        print('[Error] Wrong mode!')
        exit()
except Exception as e:
    print(e)
    exit()

if res is not None:
    print(res)
