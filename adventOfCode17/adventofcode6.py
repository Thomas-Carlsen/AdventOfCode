# banks = [0, 2, 7, 0] #test
banks = [10,	3,	15,	10,	5,	15,	5,	15,	9,	2,	5,	8,	5,	2,	3,	6] # input

redistribution = []
redistribution.append(banks)

cycles = 0


#print(banks, "len: ", len(banks), redistribution)

'''
while True:
	maxest = max(banks)
	index = banks.index(maxest)
	banks = [x for x in banks]
	banks[index] = 0
	for c in range(1,1+maxest):
		banks[(index+c)%len(banks)] += 1
	cycles += 1
	#print(banks, maxest)
	if banks in redistribution:
		break
	redistribution.append(banks)
'''
# 1 solved
# print(cycles)



# banks = [0, 2, 7, 0] #test
banks = [10,	3,	15,	10,	5,	15,	5,	15,	9,	2,	5,	8,	5,	2,	3,	6] # input



redistribution = []
redistribution.append(banks)

cycles = 0


# print(banks, "len: ", len(banks), redistribution)


while True:
	maxest = max(banks)
	index = banks.index(maxest)
	banks = [x for x in banks]
	banks[index] = 0
	for c in range(1,1+maxest):
		banks[(index+c)%len(banks)] += 1
	cycles += 1
	#print(banks, maxest)
	if banks in redistribution:
		redistribution.append(banks)
		break
	redistribution.append(banks)

# 2 solved
last = redistribution[-1]
index = redistribution.index(last)
print(len(redistribution)-1 - index)



