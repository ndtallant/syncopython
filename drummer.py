'''
Classes that form the basis for syncopython
The rhythm string for each limb will be parsed and joined
to output to drumseq.py as I develop a backend.
'''

class Limb:
    '''
    Limb object has a MIDI sound #, RhythmString, and label.
    '''

    def __init__(self, patch, rs, label):
        self.patch = patch
        self.rhythm = rs
        self.label = label

    def __repr__(self):
        return '{} "{}" {}'.format(self.patch, self.rhythm, self.label)

RH = Limb(42, '1 &, 2 &, 3 &, 4 &', 'HH')
LH = Limb(38, '   , 2  ,    , 4  ', 'Snare')
RF = Limb(36, '1  ,   &, 3  ,   &', 'Kick')
LF = Limb(42, '   , 2  ,    , 4  ', 'Foot')

class Drummer:
    '''
    A collection of 4 limbs with defaults set.
    '''

    # pre-pairing init
    # def __init__(self, right=RH, left=LH, rfoot=RF, lfoot=LF):
    #     self.RH = right
    #     self.LH = left
    #     self.RF = rfoot
    #     self.LF = lfoot
    #     self.limbs = [self.RH, self.LH, self.RF, self.LF]

    def __init__(self, input_stream=None, **kwargs):
        if input_stream:
            self.feed(input_stream)

    def feed(new_input): # new_input should be a readable stream (or string)
        '''
        parse new_input and modify internal state accordingly
        modify internal state according to new input
        '''
        return NotImplementedError

    def output_drumseq(self):
        '''
        TODO
        generates pattern suitable for drumseq.Sequencer
        based on current internal state
        '''
        raise NotImplementedError

    def __repr__(self):
        for limb in self.limbs:
            print('{} {} {}'.format(limb.patch, limb.rhythm, limb.label))
