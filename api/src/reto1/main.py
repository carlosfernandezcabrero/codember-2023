import os

fp = os.path.dirname(__file__)
input_url = "https://codember.dev/data/message_01.txt"

def solution():
    with open(f"{fp}/input.txt") as input:
        r = {}

        for i in input.read().split():
            r[i] = r.get(i, 0) + 1

        d = [f"{k}{v}" for k, v in r.items()]

        return ("").join(d)
