# Making a basic drum beat in mido

import time
import mido
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(mido.get_output_names())
#if available_ports:
#    midiout.open_port('TiMidity port 0')
with mido.open_output(mido.get_output_names()[1]) as output:
 
    note_on = mido.Message('note_on', channel=9, note=60, velocity=112).bytes()
    note_off = mido.Message('note_off', channel=9, note=60, velocity=0).bytes()

    output.send(note_on)
    time.sleep(5)
    output.send(note_off)

#midiout.send_message(note_on)
#time.sleep(5)
#midiout.send_message(note_off)

#del midiout

