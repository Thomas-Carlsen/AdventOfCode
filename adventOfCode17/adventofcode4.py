f = open("input4.txt", "r")

validCount = 0


def checkValidity(line):
	s = line.split()
	v = "valid"
	for s1 in s:
		i = s.index(s1) + 1
		for s2 in s[i:]:
			if s1 == s2:
				v = "invalid"
	return v


for line in f:
	if checkValidity(line) == "valid":		
		validCount += 1

# solved 1
#print(validCount)

#print(checkValidity("aa bb cc dd aaa"))
#aa bb cc dd ee - valid
#aa bb cc dd aa - invalid
#aa bb cc dd aaa - valid




f = open("input4.txt", "r")
validCount = 0


def checkValidity(line):
	s = line.split()
	v = "valid"
	for s1 in s:
		i = s.index(s1) + 1
		s1_splited = list(s1)
		for s2 in s[i:]:
			if sorted(s1) == sorted(s2):
				v = "invalid"
	return v


for line in f:
	if checkValidity(line) == "valid":		
		validCount += 1

# solved 2
print(validCount)

print(checkValidity("bdwdjjo avricm cjbmj ran lmfsom ivsof"))
#abcde fghij - valid
#abcde xyz ecdab - invalid
#a ab abc abd abf abj - valid
#iiii oiii ooii oooi oooo - valid
#oiii ioii iioi iiio - invalid

