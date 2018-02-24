#!/usr/bin/env python3

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
    Will instatiate the drumseq sequencer with the 
    parsed pattern from user input (shell).
    '''

    def __init__(self, port_desc='TiMidity port 0', **kwargs):
        self.port = port
    def __enter__(self):
        pass
    def __exit__(self):
        pass
if __name__ == "__main__":
    import docopt
    # look at docopt docs
    arguments = docopt.docopt(HELP, version='Syncoi v0.1')
    # optionally transform our input file to what drumseq.Sequencer expects

    if arguments['midi']:
         output = MidiOut(**arguments)
    print(arguments)

