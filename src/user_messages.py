class myColors:
    SYNCO = '\033[33m' 
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_screen():
    message = (myColors.SYNCO +' \n'
               ' ' + '-'*41 + ' \n'
               '|' + ' '*41 + '|\n'
               '|' + ' '*41 + '|\n'
               '|' + ' '*15 + 
                     myColors.UNDERLINE + 
                     ' SYNCOPYTHON ' 
                     + myColors.ENDC +
                     myColors.SYNCO + 
                     '             |\n'
               '|' + ' '*41 + '|\n'
               '|' + ' '*41 + '|\n'
               '|        A text based drum machine.       |\n'
               '|' + ' '*41 + '|\n'
               '|' + ' '*41 + '|\n'
               ' ' + '-'*41 + ' \n\n'
               '       Type ' + myColors.GREEN + '"help"'
                              + myColors.SYNCO + ' to see commands.\n')
    print(message)

def get_help():
    message = ('\n\n'
               'Commands:\n'
               '          Examples     \n'
               '          Add Instrument     \n'
               '          Delete Instrument  \n'
               '          Change Instrument  \n'
               '          play               \n'
               '          exit               \n\n'
               'Instruments:                 \n'
               '          Hi-Hat \n'
               '          Snare \n'
               '          Kick  \n\n'
               'Notation Ex:\n'
               '          1e&a, 2&, 3e a, 4 \n'
               '          1   ,   ,3    , 4 \n')
    print(message)

def get_examples():
    message = ('\n\n'
               '> Add Instrument \n'
               '    Instrument > Hi-Hat \n'
               '         Rhythm > 1&,2&,3&,4& \n\n'
               '> Add Instrument \n'
               '    Instrument > Snare \n'
               '         Rhythm > ,2, ,4 \n\n'
               '> Add Instrument \n'
               '    Instrument > Kick \n'
               '         Rhythm > 1&, , 3e a, \n\n'
               '> See Drumkit \n'
               '         Hi-Hat: "1&,2&,3&,4&" \n'
               '         Snare: ",2, ,4" \n'
               '         Kick: "1&, , 3e a," \n\n')

    print(message)
