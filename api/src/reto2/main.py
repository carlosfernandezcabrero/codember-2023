import os

fp = os.path.dirname(__file__)
input_url = "https://codember.dev/data/message_02.txt"

INCREMENT_ONE = "#"
DECREMENT_ONE = "@"
MULTIPLY_SELF = "*"
PRINT_VALUE = "&"


def solution():
    o = ""
    v = 0

    with open(f"{fp}/input.txt") as input:
        for i in input.read():
            if i == PRINT_VALUE:
                o += str(v)
            if i == INCREMENT_ONE:
                v += 1
            if i == DECREMENT_ONE:
                v -= 1
            if i == MULTIPLY_SELF:
                v *= v

    return o
