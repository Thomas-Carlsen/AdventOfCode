import string

# Setup

f = open("2.txt", "r")
ids = []

for id in f:
    ids.append(id.strip())

# First Star
counts = {"2":0, "3":0}

for id in ids:
    counter = [id.count(letter) for letter in string.ascii_lowercase]
    if 2 in counter: counts["2"] += 1
    if 3 in counter: counts["3"] += 1

checksum = counts["2"] * counts["3"]

print("First Star:", checksum)


# Second Star
def findPrototypeBox():
    for i, id in enumerate(ids):
        l = ids[:i] + ids[i+1:]
        for j in range(len(id)):
            current_id = id[:j] + id[j+1:]
            if current_id in [box_id[:j] + box_id[j+1:] for box_id in l]:
                return current_id

print("Second Star:", findPrototypeBox())