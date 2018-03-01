#!/usr/bin/env python

import opc, time

client = opc.Client('localhost:7890')

NUM_LEDS = 512

# define aggregate colors
COLOR_ALL_BLACK = [ (0,0,0) ] * NUM_LEDS
COLOR_ALL_WHITE = [ (255,255,255) ] * NUM_LEDS

# define individual colors
COLOR_BLACK = (0,0,0)
COLOR_GREY = (127,127,127)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)

# custom colors
blue1 = [ (0,66,200) ] * NUM_LEDS
blue2 = [ (8,0,65) ] * NUM_LEDS
blue3 = [ (120,120,255) ] * NUM_LEDS # white-ish blue

red1 = [ (120,120,255) ] * NUM_LEDS

yellow = [ (255,,0) ] * NUM_LEDS

client.put_pixels(yellow)