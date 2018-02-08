class RhythmString(object):
    '''
    This object converts a string into MIDI output. 
        `String syntax:
            "1e&a 2e&a 3e&a 4e&a"
            "1 &a 2e a 3 &  4e&a"
            The actual details of this depend on
            how I end up parsing it.
    '''

    def __init__(self, rhythm, tempo=88):
        self.rhythm = rhythm
        self.tempo = tempo
    
    @property
    def tempo(self):
        return self._tempo
    
    @tempo.setter
    def tempo(self, tempo):
        if not isinstance(tempo, int) or tempo < 0:
            raise ValueError("Great drummers use a positive integer \
                    for tempo")
        self._tempo = tempo

    def __repr__(self):
        return self.rhythm
