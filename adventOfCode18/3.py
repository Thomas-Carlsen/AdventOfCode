import re

f = open("3.txt", "r")

claims = []
inches = 0
max_width = 0
max_height = 0
ids = []

for l in f:
    [id, left, top, width, height] = [int(x) for x in re.findall("\d+", l)]
    ids.append(id)
    if left + width > max_width:
        max_width = left + width
    if top + height > max_height:
        max_height = top + height
    claims.append([left, top, width, height])

matrix = []
for i in range(max_height):
    matrix.append("." * max_width)

for claim in claims:
    [left, top, width, height] = claim
    for k in range(top, top + height ):
        for j in range(left, left + width ):
            if matrix[k][j] == "x":
                matrix[k] = matrix[k][:j] + "1" + matrix[k][j+1:]
                inches += 1

                idx = claims.index(claim)
                for cl in claims[:idx] + claims[idx+1:]:
                    [l, t, w, h] = cl
                    if l <= j <= w+l and t <= k <= t+h:
                        if idx+1 in ids:
                            ids.pop(ids.index(idx+1))
                        if claims.index(cl)+1 in ids:
                            ids.pop(ids.index(claims.index(cl)+1))

                
            if matrix[k][j] == ".":
                matrix[k] = matrix[k][:j] + "x" + matrix[k][j+1:]


print(inches)
print(ids)

'''
def noOverLap(claim, oc, idx):
    [l, t, w, h] = claim
    [l_oc, t_oc, w_oc, h_oc] = c
    
    if l < l_oc < 
    
    

the_one = None
for claim in claims:
    idx = claims.index(claim)
    cs = claims[:idx] + claims[idx+1:]
    # oc for other claim
    for oc in cs:
        print(noOverLap(claim, oc, idx))
'''