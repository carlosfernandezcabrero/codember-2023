import os

import requests

fp = os.path.dirname(__file__)
input_url = "https://codember.dev/data/message_01.txt"

def solution(input):
    r = {}

    for i in input.split():
        r[i] = r.get(i, 0) + 1

    d = [f"{k}{v}" for k, v in r.items()]

    return ("").join(d)
