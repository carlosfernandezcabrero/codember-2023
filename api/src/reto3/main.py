input_url = "https://codember.dev/data/encryption_policies.txt"


def solution(input):
    n = 0

    for line in input.splitlines():
        policy, password = line.split(": ")
        limits, letter = policy.split(" ")
        min, max = limits.split("-")

        if not (int(min) <= password.count(letter) <= int(max)):
            n += 1

        if n == 42:
            return password
