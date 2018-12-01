f = open("input5.txt", "r")

s = ""
steps = 0
index = 0

for line in f:
	s = s + line
inpt = s.split()
inpt = [int(x) for x in inpt]
# print("start: ", inpt)

def jumpAround(inpt, index, steps):
	jump_to = inpt[index] + index
	inpt[index] += 1
	steps += 1
	return inpt, steps, jump_to
	
while 1==1:
	inpt, steps, index = jumpAround(inpt, index, steps)
	if index < 0 or index > len(inpt) - 1:
		break

# 1 solved
# print(steps)




f = open("input5.txt", "r")

s = ""
steps = 0
index = 0

for line in f:
	s = s + line
inpt = s.split()
inpt = [int(x) for x in inpt]
# print("start: ", inpt)

def jumpAround(inpt, index, steps):
	jump_to = inpt[index] + index
	if inpt[index] >= 3: 
		inpt[index] -= 1
	else:
		inpt[index] += 1
	steps += 1
	return inpt, steps, jump_to
	
while True:
	inpt, steps, index = jumpAround(inpt, index, steps)
	if index < 0 or index > len(inpt) - 1:
		break

print(steps)




