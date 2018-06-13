#!/usr/bin/env python3

import time
import docopt
import rtmidi
import threading
from rtmidi.midiutil import open_midioutput

# syncopython 
from . import drumseq
from . import transcription

class SyncoSequencer(drumseq.Sequencer):
    ''' 
    Wrapper around drumseq's Sequencer object which has an API
    closer to what we want to use 
    '''
    def __init__(self, midiout, pattern, bpm=100, channel=9, volume=127):
        super().__init__(midiout, pattern, bpm, channel, volume)
        self.midiout = midiout
        self.bpm = max(20, min(bpm, 400))
        self.interval = 15. / self.bpm
        self.pattern = drumseq.Drumpattern(pattern)
        self.channel = channel
        self.volume = volume

    def play(self):
        ''' 
        This extends from drumseq which extends from thread which has this method. 
        Make a new thread for the output and control it 
        ''' 
        self.start()
    
    def update_bar(self, current_bar):
        print('current bar from DreamSequencer.update_bar:', current_bar)

    def stop(self):
        '''Join closes the loop so user can input again''' 
        self.done = True
        self.join()

class MidiOut(): 
    '''
    Will instatiate the drumseq.Sequencer with the
    parsed pattern from user input (shell).
    and play notes when .play() is called
    '''

    def __init__(self, t=None, user_port=None, **kwargs):
        '''
        This will take most of the functionality of __enter__
        i.e. - it will load an instance of the seqquencer with the pattern.
        Play will actually call sequencer (see below)
        '''
        if t:
            self.drumseq_pattern = t.output_drumseq() 
        else: 
            raise TypeError('Must have instruments to play!')
        try:
            midiout, port_name = open_midioutput(
               '1', # this is the output port, use 'fluid' if using fluidsynth 
                port_name="MIDI Out",
                api=rtmidi.API_RTMIDI_DUMMY,    # APIs: 
                client_name="syncopython",      #    LINUX_ALSA - worked, still a prompt
                use_virtual=False)              #    RTMIDI_DUMMY - worked, still a prompt
        except (EOFError, KeyboardInterrupt):   
            pass
        
        self.sequencer = SyncoSequencer(midiout, self.drumseq_pattern)

    def __enter__(self): 
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        '''
        catches errors and handles them a certain way
        Clean up transcription, midi ports, etc.
        you can re raise the exception here to see what happened
        '''
        self.stop()

    def stop(self):
        self.sequencer.stop()

    def play(self):
        '''
        Takes the output_str from the Transcription class
        and runs it through drumseq.

        try the start method in drumseq.orig
                start extends the Thread method
            whatever actually makes the thing run
        '''
        
        # print("Playing drum loop at %.1f BPM, press Control-C to quit." % self.sequencer.bpm)
        
        self.sequencer.play()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print('')
        finally:
            self.stop()
