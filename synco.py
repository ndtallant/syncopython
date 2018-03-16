#!/usr/bin/env python3
from transcription import Transcription, RhythmString 
import drumseq

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

class MidiOut():
    '''
    Will instatiate the drumseq.Sequencer with the
    parsed pattern from user input (shell).
    and play notes when .play() is called
    '''

    def __init__(self, input_pattern=None, port_desc='TiMidity port 0', **kwargs):
        if len(input_pattern) == 0:
            raise TypeError('must have input_pattern to play!')
        self.port = port_desc #Double check a string is what this needs
        self.drumseq_pattern = self.parse_drummer(input_pattern)

    def parse_drummer(self, input_pattern):
        # Have Transcription object parse and return
        # drumseq_pattern
        pass
    def __enter__(self): # Review what these are
        pass
    def __exit__(self):
        pass

    def play(self):
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
    import docopt
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

    output_class = None
    if arguments['-o'] or arguments['--output']:
        output_class = MidiFileOut
    else:
        output_class = MidiOut

    with output_class(drumseq_pattern=drumseq_pattern) as out:
        out.play()
