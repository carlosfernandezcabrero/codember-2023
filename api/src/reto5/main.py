import csv
import re

input_url = "https://codember.dev/data/database_attacked.txt"


def solution(input):
    out = ""

    for row in input.splitlines():
        if not re.match(
            r"^[a-zA-Z\d]+,[a-zA-Z\d]+,[\w\d]*@[a-z]*\.[a-z]*,[\d]*,[a-zA-Z\d\s]*$",
            row.strip(),
        ):
            out += row.split(",")[1][0]

    return out
