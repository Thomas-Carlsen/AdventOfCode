from itertools import accumulate, cycle

f = open("1.txt", "r")

# First Star
changes = [int(n) for n in f]
print("First:", sum(changes))

# Second Star
seen = set()
print("Second:", next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))