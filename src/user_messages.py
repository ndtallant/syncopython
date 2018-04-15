def load_screen():
    message = ('\n'
               ' ----------------------------------------- \n'
               '|                                         |\n'
               '|                                         |\n'
               '|                SYNCOPYTHON              |\n'
               '|                -----------              |\n'
               '|                                         |\n'
               '|        A text based drum machine.       |\n'
               '|                                         |\n'
               '|                                         |\n'
               ' ----------------------------------------- \n\n'
               '       Type "help" to see commands.        \n')
    print(message)

def get_help():
    message = ('\n\n'
               'Commands:\n'
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

