'''
Classes that form the basis for syncopython.

The rhythm string for each limb will be parsed and joined
to output to drumseq.py as I develop a backend.
'''

import re

class RhythmString:
    '''
    RhythmString object has a MIDI sound #, RhythmString, and label.
    '''

    def __init__(self, patch, rs, label):
        self.patch = patch
        self.rhythm = rs
        self.label = label

    def __str__(self):
        return '{} "{}" {}'.format(self.patch, self.rhythm, self.label)

class Transcription:
    '''
    Class that parses syncopython notation -> drumseq.

    This class parses a multiline string into RhythmStrings, 
    and parses a collection of RhythmStrings back into a
    multiline string to be handled by the backend.
    '''

    def __init__(self, input_str=None, **kwargs):
        self.stack = []

        if input_str:
            print(input_str) #getting extra positional argument
            self.feed(input_str)

    def feed(self, new_input): 
        '''
        Parse new_input and modify internal state accordingly.
        Modify internal state according to new input.
        '''
        for item in new_input.split('\n'):
            patch, rs, label = item.split('|')
            self.stack.append(RhythmString(patch, rs, label))
        # Not sure if I want to have a fresh stack each time

    def output_drumseq(self):
       '''
       Generate pattern suitable for drumseq.Sequencer
       based on current internal state
       '''
       rv = '#  1...2...3...4...\n'
       for r in self.stack: # need \n between RS?
          ds_rhythm = self.drumseq_helper(r.rhythm) 
          rv += '{}{} {}\n'.format(r.patch, ds_rhythm, r.label) 
       return rv
        
    def drumseq_helper(self, rhythm):
       rv = ''
       for beat in rhythm.split(','):
           rv += self.beat_parse('\d', beat)
           rv += self.beat_parse('e', beat)
           rv += self.beat_parse('&', beat)
           rv += self.beat_parse('a', beat)
       return rv    

    def beat_parse(self, exp, beat):
       return 'x' if re.search(exp, beat) else '.'

if __name__ == "__main__":
     RH = RhythmString(42, '1 &, 2 &, 3 &, 4 &', 'HH')
     LH = RhythmString(38, '   , 2  ,    , 4  ', 'Snare')
     RF = RhythmString(36, '1  ,   &, 3  ,   &', 'Kick')
     LF = RhythmString(42, '   , 2  ,    , 4  ', 'Foot')
