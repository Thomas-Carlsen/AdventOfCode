from collections import *
import itertools
import random
import sys
from string import ascii_uppercase, ascii_lowercase
import re

f = open("6.txt")

points = []

min_l = 1000
max_r = 0
min_t = 1000
max_b = 0

for l in f:
    l = l.strip().split(",")
    x, y = int(l[0]), int(l[1])
    if x < min_l:
        min_l = x
    if x > max_r:
        max_r = x
    if y < min_t:
        min_t = y
    if y > max_b:
        max_b = y
    points.append([x,y])

manhattan = [["."]*(max_r+1) for _ in range(max_b+1)]

'''
print(min_l)
print(max_r)
print(min_t)
print(max_b)
'''

'''
for l in manhattan:
    print(l)
'''

'''
for i, point in enumerate(points):
    x, y = point[0], point[1]
    #print(x, y)
    manhattan[y][x] = "A"*(i+1)


def markDistFromPoint(idx, p):

    for i in range(max_r +1):
        for j in range(max_b + 1):
            mark = manhattan[j][i]
            dist = abs(j - p[1]) + abs(i - p[0])
            alp = "a" * (idx+1)
            if mark == ".":
                manhattan[j][i] = alp + str(dist)

            elif re.findall("\d+", mark) != []:
                num = int(re.findall("\d+", mark)[0])
                if dist < num: manhattan[j][i] = alp + str(dist)
                elif dist == num: manhattan[j][i] = str(dist)


for i, p in enumerate(points):
    markDistFromPoint(i, p)

infinite_letters = []

def findLetterHorizontally(lizt):
    for l in lizt:
        letter = re.findall("a+", l)
        if letter != []:
            if letter[0] not in infinite_letters:
                infinite_letters.append(letter[0])

def findLetterVertically(man, i):
    for v in man:
        for l in v[i]:
            letter = re.findall("a+", l)
            if letter != []:
                if letter[0] not in infinite_letters:
                    infinite_letters.append(letter[0])

findLetterHorizontally(manhattan[0])
findLetterHorizontally(manhattan[-1])
findLetterVertically(manhattan, 0)
findLetterVertically(manhattan, len(manhattan[0])-1)

areas = []


for i, p in enumerate(points):
    letter = "a"*(i+1)
    count = 1
    if letter not in infinite_letters:
        for j in range(max_r + 1):
            for k in range(max_b + 1):
                l = manhattan[k][j]
                if re.findall("a+", l) != []:
                    id = re.findall("a+", l)[0]
                    if id == letter: count += 1
    areas.append(count)

print(areas)
print(max(areas))
'''

# Second Star
counter = 0
for i in range(max_r + 1):
    for j in range(max_b + 1):
        total_dist_from_point = 0
        for p in points:
            mark = manhattan[j][i]
            dist = abs(j - p[1]) + abs(i - p[0])
            total_dist_from_point += dist
        if total_dist_from_point < 10000:
            counter += 1
            manhattan[j][i] = total_dist_from_point


print(counter)
