#!/usr/bin/env python

import opc, time, random, csv

client = opc.Client('localhost:7890')

numLEDs = 512
startIndex = 448 #first light connected to pin 7 starts at index 448

# define aggregate colors
allBlack = [ (0,0,0) ] * numLEDs
allWhite = [ (255,255,255) ] * numLEDs

# define individual colors
black = (0,0,0)
grey = (100,100,100)
white = (255,255,255)
red = (255,0,0)

# before doing anything, load in black
client.put_pixels(allBlack)

# read in data file
infile = open('time-of-crime-processed.csv','rb')
reader = csv.reader(infile)

"""
- build an in-memory map of (minute, [dates])
- loop through every minute of the year
- for each minute, if there are applicable dates, light up
	(there are 60*24*365 = 525,600 minutes in a year)

row[3]: minutes since start of day
row[0]: date as integer
"""

# initialize dictionary with lists as values
data = {k: [] for k in range(1440)}

# go through csv input file. per row, add mapping for minutes-since-SOD to crime dates
for row in reader:
	data[row[3]].append(row[0])

# iterate through minutes of the day
for minute in range(1440):
	# check if the list at data[minute] is non-empty
	if data[minute]:
		pixels = list(allBlack)
		for crimeDate in data[minute]:
			# set color for lights whose indices correspond to those dates
			pixels[crimeDate] = white;
		# load in data to lights
		client.put_pixels(pixels)


"""
for i in range(60):
	time.sleep(1)
	pixels = list(allBlack)
	
	int1 = random.randint(448,458)
	int2 = random.randint(448,458)
	int3 = random.randint(448,458)
	print(int1, int2, int3)

	pixels[int1] = (255,0,0)
	pixels[int2] = (0,255,0)
	pixels[int3] = (0,0,255)
	
	client.put_pixels(pixels)
"""