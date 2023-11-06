import os

fp = os.path.dirname(__file__)

print(fp)

with open(f"{fp}/input.txt") as input:
    r = {}
    
    for i in input.read().split():
        r[i] = r.get(i, 0) + 1
    
    d = [f"{k}{v}" for k, v in r.items()]
    print(("").join(d))