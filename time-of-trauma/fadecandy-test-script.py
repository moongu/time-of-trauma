#!/usr/bin/env python

import opc, time, random

numLEDs = 512
startIndex = 448 - 64 #first light connected to pin 6 starts at index 448-64
endIndex = 448 + 30
client = opc.Client('localhost:7890')

allBlack = [ (0,0,0) ] * numLEDs
allWhite = [ (255,255,255) ] * numLEDs

black = (0,0,0)
grey = (100,100,100)
white = (255,255,255)
red = (255,0,0)

# load in black
client.put_pixels(allBlack)



"""
# fade into white at second pixel
pixels = list(allBlack)
pixels[startIndex+2] = grey
time.sleep(2)
client.put_pixels(pixels)

# fade into red
pixels[startIndex+2] = red
time.sleep(2)
client.put_pixels(pixels)

# fade into black
time.sleep(2)
client.put_pixels(allBlack)
"""


for i in range(60):
	time.sleep(1)
	pixels = list(allBlack)
	
	int1 = random.randint(startIndex, endIndex)
	int2 = random.randint(startIndex, endIndex)
	int3 = random.randint(startIndex, endIndex)
	print(int1, int2, int3)

	pixels[int1] = (255,0,0)
	pixels[int2] = (0,255,0)
	pixels[int3] = (0,0,255)
	
	client.put_pixels(pixels)