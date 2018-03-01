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
        return '{} "{}" {}/
               '.format(self.patch, self.rhythm, self.label)

class Drummer:
    '''
    A collection of 4 limbs with defaults set.
    '''    

    def __init__(self, right=RH, left=LH, rfoot=RF, lfoot=LF):
        self.RH = right
        self.LH = left
        self.RF = rfoot
        self.LF = lfoot
        self.limbs = [self.RH, self.LH, self.RF, self.LF]

    def parse_rhythm(self):
        pass    

    def __repr__(self):
        for limb in self.limbs:
            print('{} {} {}'.format(limb.patch, limb.rhythm, limb.label)

if name == "__main__":
     RH = Limb(42, '1 &, 2 &, 3 &, 4 &', 'HH')
     LH = Limb(38, '   , 2  ,    , 4  ', 'Snare')
     RF = Limb(36, '1  ,   &, 3  ,   &', 'Kick')
     LF = Limb(42, '   , 2  ,    , 4  ', 'Foot')

   
