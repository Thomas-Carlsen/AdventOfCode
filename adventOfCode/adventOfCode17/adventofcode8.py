
f = open("input8_test.txt","r")

ins = []
regs = []

for line in f:
	ins.append(line.split())

for i in ins:
	if [i[0],0] not in regs:
		regs.append([i[0],0])

def lookupRegVal(reg):
	for r in regs:
		if r[0] == reg:
			return r[1]
	return int(reg)

def cond_holds(conds):
	l = lookupRegVal(conds[0])
	r = lookupRegVal(conds[2])
	res = False
	if conds[1] == "==":
		res = (l == r)
	elif conds[1] == "!=":
		res = (l != r)
	elif conds[1] == "<":
		res = (l < r)
	elif conds[1] == "<=":
		res = (l <= r)
	elif conds[1] == ">":
		res = (l > r)
	elif conds[1] == ">=":
		res = (l >= r)
	return res

def find_reg_index(reg):
	for i in range(len(regs)):
		r = regs[i]
		if r[0] == reg:
			return i

maxest = 0
def maxReg():
	temp = []
	for r in regs:
		temp.append(r[1])
	if max(temp) > maxest: maxest = max(temp)
	return max(temp)

def readIns(ins):
	for i in ins:
		# print(i)
		if cond_holds(i[4:]):
			reg_index = find_reg_index(i[0])
			reg = regs[reg_index]
			if i[1] == "inc":
				reg[1] += int(i[2])
			elif i[1] == "dec":
				reg[1] -= int(i[2])
		maxReg()
readIns(ins)


		
print(regs)
# 1 solved
print(maxReg())

print(maxest)


