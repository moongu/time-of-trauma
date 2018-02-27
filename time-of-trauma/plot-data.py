#!/usr/bin/env python

import opc, time, random, csv

client = opc.Client('localhost:7890')

NUM_LEDS = 512
DATE_OFFSET = 129 #the first day of the year corresponds to LED index 129

# define aggregate colors
COLOR_ALL_BLACK = [ (0,0,0) ] * NUM_LEDS
COLOR_ALL_WHITE = [ (255,255,255) ] * NUM_LEDS

# define individual colors
COLOR_BLACK = (0,0,0)
COLOR_GREY = (127,127,127)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)

# define delay between looping through minutes
DELAY = 0.5

# before doing anything, load in black
client.put_pixels(COLOR_ALL_BLACK)

"""
# test: index range of each strip
pixels = list(COLOR_ALL_BLACK)

strip1 = 448 - 64
strip2 = 448
strip3 = 448 + 30

pixels[int1] = (255,0,0)
pixels[int2] = (0,255,0)
pixels[int3] = (0,0,255)

client.put_pixels(pixels)
"""

# read in data file
infile = open('time-of-crime-processed.csv','r')
reader = csv.reader(infile)

"""
Notes:
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
	data[int(row[3])].append(int(row[0]))

infile.close()
print('Finished building data map!')


# iterate through minutes of the day
for minute in range(1440):
	time.sleep(DELAY)
	print("minute:", minute)
	# check if the list at data[minute] is non-empty
	if data[minute]:
		"""
		# test: turn on random lights in different colors 
		LED_START_INDEX = 384 #first light connected to pin 6 starts at 448 - 64
		LED_END_INDEX = 448 + 29 + 31
		pixels = list(COLOR_ALL_BLACK)
		int1 = random.randint(LED_START_INDEX, LED_END_INDEX)
		int2 = random.randint(LED_START_INDEX, LED_END_INDEX)
		int3 = random.randint(LED_START_INDEX, LED_END_INDEX)
		pixels[int1] = (255,0,0)
		pixels[int2] = (0,255,0)
		pixels[int3] = (0,0,255)
		client.put_pixels(pixels)
		"""
		print('crimes at minute', minute, data[minute])
		
		pixels = list(COLOR_ALL_BLACK)
		for crimeDate in data[minute]:
			# set color for lights whose indices correspond to those dates
			pixels[DATE_OFFSET + crimeDate] = COLOR_WHITE
		
		# load in data to lights
		client.put_pixels(pixels)
	else:
		client.put_pixels(COLOR_ALL_BLACK)
	time.sleep(DELAY)