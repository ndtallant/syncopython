#!/usr/bin/env python

import random
import mido

class hit(mido.Message):
    def __init__(self, type):
        #self.channel = 9
        #self.note = note
        #self.velocity = velocity
        #self.time = time
        super()

outfile = mido.MidiFile()
track = mido.MidiTrack()
outfile.tracks.append(track)
track.append(mido.Message('program_change', program=52))
'''
kick_on = hit(note=35, velocity=122, time=122)
off = mido.Message('note_off', channel=9, note=42, velocity=0, time=122)
hat_on = hit(note=42, velocity=80,time=122)
snare_on = hit(note=38, velocity=100, time=122)

def kick():
    track.append(kick_on)
    track.append(off)

def hat():
    track.append(hat_on)
    track.append(off)

def snare():
    track.append(snare_on)
    track.append(off)

for i in range(40):
    kick()
    hat()
    snare()
    hat()

outfile.save('beat.mid')

with mido.open_output('TiMidity port 0') as output:
    for message in mido.MidiFile(filename).play():
        output.send(message)
'''
