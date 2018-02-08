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

class Drummer(object):
    '''
    This object is a collection of 4 RhythmStrings.
    Lots of defaults to come!
    '''

    def __init__(self, RH="eighths", 
                       LH="2 4", 
                       RF="1 3", 
                       LF="quarters",
                       tempo=88):

        self.RH = RhythmString(RH,tempo)
        self.LH = RhythmString(LH,tempo)
        self.RF = RhythmString(RF,tempo)
        self.LF = RhythmString(LF,tempo)
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
        self.RH.tempo = tempo
        self.LH.tempo = tempo
        self.RF.tempo = tempo
        self.LF.tempo = tempo
