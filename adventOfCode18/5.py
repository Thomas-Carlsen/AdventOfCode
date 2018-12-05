
f = open("5.txt", "r")
from string import ascii_lowercase
polymer_original = f.readline().strip()


leng = len(polymer_original)
lowest = leng
for l in ascii_lowercase:
    can_reduce = True
    i = 0
    polymer = polymer_original.replace(l.upper(), "").replace(l.lower(), "")
    while can_reduce:
        prev_char = polymer[i]
        c = polymer[i + 1]
        if prev_char != c and (prev_char.upper() == c or prev_char.lower() == c):
            polymer = polymer[:i] + polymer[i+2:]
            i = i - 1
        if i + 2 >= len(polymer):
            i = 0
            if leng == len(polymer):
                can_reduce = False
            leng = len(polymer)
        else:
            i = i + 1

    if len(polymer) < lowest:
        lowest = len(polymer)


print(lowest)