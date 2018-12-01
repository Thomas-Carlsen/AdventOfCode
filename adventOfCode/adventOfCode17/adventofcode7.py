import numpy as np
import re

f = open("input7.txt", "r");


towers = []
names = []
lifters = []

for line in f:
	towers.append(re.split(", | | \n| \t", line))

for elem in towers:
	names.append(elem[0])
	if len(elem) > 2:
		if elem[2] == "->":
			lifters.append(elem)


for l in lifters:
	for r in l[3:]:
		if r.rstrip() in names:
			names.remove(r.rstrip())
	

# solved 1
print(names)


def getFullElement(name):	
	for l in towers:
		if l[0] == name:
			return l
# r = getFullElement('tknk')
r = getFullElement('ahnofa')

def printChrildren(node):
	for c in node[3:]:
		print(getFullElement(c.rstrip()))

final = 0

def checkBalance(balance, node):
	count = 0
	unbalanced = 0
	other = 0
	got_him = False
	for i in range(len(balance)):
		b1 = balance[i]
		for j in range(len(balance)):
			b2 = balance[j]
			if i != j:
				if b1 != b2:
					count += 1
					if count == 2:
						unbalanced = i
						other = j
						got_him = True
	if got_him:
		print(unbalanced, other, balance[unbalanced], balance[other], "------------HER-----------")
		kids = node[3:]
		unbalanced_child = getFullElement(kids[unbalanced])
		weight = unbalanced_child[1].rstrip()
		weight = int(weight[1:-1])
		if balance[unbalanced] > balance[other]:
			print(weight - (balance[unbalanced]-balance[other]))
		else:
			print(weight + (balance[other]-balance[unbalanced]))
			

def getBalance(node):
	if node in lifters:
		weight = node[1].rstrip()
		weight = int(weight[1:-1])
		balanced = []
		for c in node[3:]:
			child = getFullElement(c.rstrip())
			balanced.append(getBalance(child))
		print(balanced)
		checkBalance(balanced, node)
		balanced.append(weight)
		return sum(balanced)
	else:
		weight = node[1].rstrip()
		weight = int(weight[1:-1])
		return weight


print(getBalance(r))


#printChrildren(r)




