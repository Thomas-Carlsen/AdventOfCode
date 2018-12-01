import math

inpoot = "347991"

# draw 25 first

# find out have many layers there are for a given number

# layer 1:1, 2:8, 3:16

# layer 3, 4 har 3 dvs. 12 resten har en dvs. da layer 2 har 8 er der 4 tilbage. Så 12 + 4 = 16

# layer 4: 12 + 12 = 24
# layer 5: 20 + 12 = 32 .. osv.


def findLayerAndLayerHeight(number):
	layer = 0
	index = 0
	if number == 1:
		layer = 1
		index = 1
	elif number in [2,3,4,5,6,7,8,9]:
		layer = 2
		index = [2,3,4,5,6,7,8,9].index(number)
	else:
		startInterval = 9+1
		endInterval = 25+1
		count = 3
		while layer == 0:
			test = [num for num in range(startInterval, endInterval)]
			if number in test:
				layer = count
				index = test.index(number)
			count += 1
			startInterval = endInterval
			endInterval = endInterval + (endInterval - 4) + 12		

	height = 1 + 2 * (layer-1)
	
	return layer, height, index


lay_res, height_res, index = findLayerAndLayerHeight(1024)

def findDistance(layer, height, index):
	middleSteps = (layer+1)
	steps_to_get_to_middle = (index+middleSteps)%height 
	return steps_to_get_to_middle + layer - 1 #tæl ikke 1 med

# first attempt to fist
# print(lay_res, height_res, index)
# print(findDistance(lay_res, height_res, index))


import numpy as np

def draw(number):
	size = int(math.sqrt(number))+1
	start_y = int(size/2)		
	start_x = start_y -1
	ma = np.zeros((size, size))
	
	y = start_y
	x = start_x
	ma[y][x] = 1
	x = x + 1
	ma[y][x] = 2
	y = y - 1
	ma[y][x] = 3
	direction = "up"
	for i in range(4,number+1):
		if direction == "up":
			if ma[y][x-1] == 0:
				direction = "left"
				x -= 1
			else:
				y -= 1
		elif direction == "left":
			if ma[y+1][x] == 0:
				direction = "down"
				y += 1
			else:
				x -= 1
		elif direction == "down":
			if ma[y][x+1] == 0:
				direction = "right"
				x += 1
			else:
				y += 1
		elif direction == "right":
			if ma[y-1][x] == 0:
				direction = "up"
				y -= 1
			else:
				x += 1
		ma[y][x] = i
	
	print(size, abs(start_y - y) + abs(start_x - x))
	return ma

# first answer
# print(draw(347991))


def sumOfAdjacent(matrix, y, x):
	m = matrix
	
	return m[y+1][x-1] + m[y+1][x] + m[y+1][x+1] + m[y][x+1] + m[y-1][x+1] + m[y-1][x] + m[y-1][x-1] + m[y][x-1]

def draw(number):
	size = int(math.sqrt(number))+3
	start_y = int(size/2)		
	start_x = start_y -1
	ma = np.zeros((size, size))
	
	y = start_y
	x = start_x
	ma[y][x] = 1
	x = x + 1
	ma[y][x] = 1
	y = y - 1
	ma[y][x] = 2
	direction = "up"
	
	for i in range(4,number+1):
		if direction == "up":
			if ma[y][x-1] == 0:
				direction = "left"
				x -= 1
			else:
				y -= 1
		elif direction == "left":
			if ma[y+1][x] == 0:
				direction = "down"
				y += 1
			else:
				x -= 1
		elif direction == "down":
			if ma[y][x+1] == 0:
				direction = "right"
				x += 1
			else:
				y += 1
		elif direction == "right":
			if ma[y-1][x] == 0:
				direction = "up"
				y -= 1
			else:
				x += 1
		
		ma[y][x] = sumOfAdjacent(ma, y, x)
		if ma[y][x] > number: break
	
	print(size, ma[y][x])
	
	return ma

# second answer
print(draw(347991))















