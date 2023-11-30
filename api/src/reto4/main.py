input_url = "https://codember.dev/data/files_quarantine.txt"


def solution(input):
    c = 0

    for i in input.splitlines():
        passphrase, checksum = i.split("-")
        pos = []

        for j in checksum:
            if j not in passphrase:
                break
            if passphrase.count(j) > 1:
                break

            pos.append(passphrase.find(j))

        if pos == sorted(pos):
            c += 1

        if c == 33:
            return checksum
