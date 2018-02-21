#!/usr/bin/env python
"""
Code taken from github.com/olemb/mido

Create a new MIDI file with some random notes.

The file is saved to test.mid.
"""
import random
from mido import Message, MidiFile, MidiTrack

notes = [36, 42, 38, 42]

outfile = MidiFile()

track = MidiTrack()
outfile.tracks.append(track)

track.append(Message('program_change', program=52))

kick_on = Message('note_on', channel=9, note=35, velocity=122, time=122)
off = Message('note_off', channel=9, note=42, velocity=0, time=122)
hat_on = Message('note_on', channel=9, note=42, velocity=80,time=122)
snare_on = Message('note_on', channel=9, note=38, velocity=100, time=122)

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

outfile.save('test.mid')
