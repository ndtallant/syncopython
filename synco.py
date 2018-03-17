#!/usr/bin/env python3

# stdlib
import threading
import time

# 3rd party
import docopt
import rtmidi
from rtmidi.midiutil import open_midioutput

# our project
import drumseq
import transcription


HELP = '''
Usage:
  synco.py -h | --help
  synco.py [ -p=PORT | --port=PORT ]
  synco.py [ -i=FILE | --input=FILE ] [-o=FILE | --output=FILE ]

Options:
  -h        --help    Show this screen.
  -i FILE,  --input   Sets the input file.
  -o FILE   --output  Sets the output file.
  -t TEMPO  --tempo   [default: 102].
  -s <arg>  --sound   [default: 'SN'].
  -p PORT   --port    [default: 'TiMiditiy port 0'].
       '''

class DreamSequencer(drumseq.Sequencer):
    ''' 
    Wrapper around drumseq's Sequencer object which
    has a desirable API.
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
        self.start()

    def stop(self):
        self.done = True
        self.join()

class MidiOut(): # check docs for this
    '''
    Will instatiate the drumseq.Sequencer with the
    parsed pattern from user input (shell).
    and play notes when .play() is called
    '''

    def __init__(self, input_pattern=None, port_desc=None, **kwargs):
        '''
        This will take most of the functionality of __enter__
        i.e. - it will load an instance of the seqquencer with the pattern.
        Play will actually call sequencer (see below)
        '''

        if not input_pattern:
            raise TypeError('must have input_pattern to play!')

        self.drumseq_pattern = self.parse_drummer(input_pattern)

        try:
            midiout, port_name = open_midioutput(
                port_desc,
                api=rtmidi.API_RTMIDI_DUMMY,
                client_name='syncopython')

        except (EOFError, KeyboardInterrupt):
            return

        self.sequencer = DreamSequencer(midiout, self.drumseq_pattern)

    def parse_drummer(self, input_pattern):
        t = transcription.Transcription(input_pattern)
        return t.output_drumseq()

    def __enter__(self): # __init__ can serve as __enter__
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

        print("Playing drum loop at %.1f BPM, press Control-C to quit." % self.sequencer.bpm)
        self.sequencer.play()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print('')
        finally:
            self.stop()

class MidiFileOut():
    '''
    Will instatiate the drumseq.Sequencer with the
    parsed pattern from user input (shell).
    and direct notes to the specified file instead of playing the notes
    '''

    def __init__(self, pattern_stream, **kwargs):
        self.output = kwargs['output']
        self.port = port
        self.pattern_stream = pattern_stream

if __name__ == "__main__":

    arguments = docopt.docopt(HELP, version='syncopython v0.1')
    
    parser = Transcription(input_pattern=arguments['--input'])
    drumseq_pattern = parser.output_drumseq()
    #print(f"drumseq_pattern: '{drumseq_pattern}'")

    OutputClass = None
    if arguments['-o'] or arguments['--output']:
        OutputClass = MidiFileOut
    else:
        OutputClass = MidiOut
    print("arguments:", arguments)

    with OutputClass(input_pattern=arguments['-i']) as out:
        origin/got-it-working
        out.play()
