#!/usr/bin/env python3
from transcription import Transcription, RhythmString 
import docopt
import drumseq_orig
import contextlib

HELP = '''
Usage:
  synco.py -h | --help
  synco.py [-p=PORT | --port=PORT]
  synco.py [ -i=FILE | --input=FILE ] [-o=FILE | --output=FILE ]

Options:
  -h       --help         Show this screen.
  -i=FILE  --input=FILE   Sets the input file.
  -o=FILE  --output=FILE  Sets the output file.
  -t=TEMPO --tempo=TEMPO  [default: 102].
  -s=<arg> --sound=<arg>  [default: 'SN'].
  -p=PORT  --port=PORT    [default: 'TiMiditiy port 0'].
       '''

class MidiOut(contextlib.AbstractContextManager): # check docs for this
    '''
    Will instatiate the drumseq.Sequencer with the
    parsed pattern from user input (shell).
    and play notes when .play() is called
    '''

    def __init__(self, input_pattern=None, port_desc='TiMidity port 0', **kwargs):
        '''
        This will take most of the functionality of __enter__ 
        i.e. - it will load an instance of the seqquencer with the pattern.
        Play will actually call sequencer (see below)
        '''

        if not input_pattern:
            raise TypeError('must have input_pattern to play!')
        
        self.port_name = port_desc #Double check this 
        self.drumseq_pattern = self.parse_drummer(input_pattern) # change name to make sense

        try:
            midiout, port_name = open_midioutput(
                args.port,
                api=rtmidi.API_RTMIDI_DUMMY, # play around with these
                client_name="syncopython",
                port_name="MIDI Out") 

        except (EOFError, KeyboardInterrupt):
            return

        seq = drumseq_orig.Sequencer(midiout, pattern, args.bpm, args.channel - 1)

        print("Playing drum loop at %.1f BPM, press Control-C to quit." % seq.bpm)

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            print('')
        finally:
            seq.done = True  # And kill it.
            seq.join()
            del midiout
        print("Done")

    def parse_drummer(self, input_pattern):
        t = Transcription(input_pattern)
        return t.output_drumseq()

    def __enter__(self): # __init__ can serve as __enter__ 
        pass

    def __exit__(self):
        '''
        catches errors and handles them a certain way
        Clean up transcription, midi ports, etc. 
        you can re raise the exception here to see what happened
        '''
        pass

    def play(self):
        '''
        Takes the output_str from the Transcription class
        and runs it through drumseq.

        try the start method in drumseq.orig
                start extends the Thread method
            whatever actually makes the thing run
        '''
        drumseq.Sequencer(pattern_stream)

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
    
    # look at docopt docs
    arguments = docopt.docopt(HELP, version='Syncoi v0.1')
    from pprint import pprint; print('arguments:'); pprint(arguments)
    # optionally transform our input file to what drumseq.Sequencer expects

    # if arguments['midi']:
    #      output = MidiOut(**arguments)
    # print(arguments)

    # pass input to parser and get something suitable for drumseq
    parser = drummer.Drummer(input_pattern=arguments['--input'])
    drumseq_pattern = parser.output_drumseq()
    print(f"drumseq_pattern: '{drumseq_pattern}'")

    # deciedes
    output_class = None
    if arguments['-o'] or arguments['--output']:
        output_class = MidiFileOut
    else:
        output_class = MidiOut

    with output_class(drumseq_pattern=drumseq_pattern) as out:
        out.play()
