import os

import requests

fp = os.path.dirname(__file__)
input_url = "https://codember.dev/data/message_02.txt"

INCREMENT_ONE = "#"
DECREMENT_ONE = "@"
MULTIPLY_SELF = "*"
PRINT_VALUE = "&"


def solution():
    o = ""
    v = 0

    for i in requests.get(input_url).text:
        if i == PRINT_VALUE:
            o += str(v)
        if i == INCREMENT_ONE:
            v += 1
        if i == DECREMENT_ONE:
            v -= 1
        if i == MULTIPLY_SELF:
            v *= v

    return o
