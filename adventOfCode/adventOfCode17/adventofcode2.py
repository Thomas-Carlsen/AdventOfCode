

f = open("input2.txt", "r")



inpoot = [ ]

for line in f:
	inpoot.append(line.split())

inpoot = [[int(j) for j in i ] for i in inpoot]


outpoot = []

outpoot = [max(inpoot[n]) - min(inpoot[n]) for n in range(len(inpoot))]


# result1
# print(sum(outpoot))




outpoot = []

n = len(inpoot)

for k in range(n):
	for i in range(len(inpoot[k])):
		for j in range(len(inpoot[k])):
			if i != j:
				if inpoot[k][i]%inpoot[k][j] == 0:
				 	outpoot.append(inpoot[k][i]/inpoot[k][j])
					
	

# result2
print(sum(outpoot))




