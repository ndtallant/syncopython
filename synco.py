#!/usr/bin/env python3

HELP = '''
Usage:
  synco <input_file> <output>  -p <port_desc> 
  synco <input_file> <output> <tempo> -f <filename>
'''

class MidiOut():
    '''
    Will instatiate the drumseq sequencer with the 
    parsed pattern from user input (shell).
    '''

    def __init__(self, port_desc='Timidity port 0', **kwargs):
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

