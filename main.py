#!/usr/bin/env python3
# File          : main.py
# Author        : Chengtao Yao
# Email         : chengtao.yao@outlook.com
# Created Time  : 2021/10/4 16:40
# Description   : crypto tools entry.


import getopt
import sys

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
                'morse2t': morse.morse_decode}

encoder_sep_dict = {'t2ascii': encoder.text_to_ascii,
                    'ascii2t': encoder.ascii_to_text}

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:m:s:', ['help', 'input', 'mode', 'sep'])
except getopt.GetoptError as e:
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
    else:
        print('[Error] Wrong mode!')
        exit()
except Exception as e:
    print(e)
    exit()


print(res)
