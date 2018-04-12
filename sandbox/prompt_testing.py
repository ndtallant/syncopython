#!/usr/bin/env python3
'''
Nick Tallant
This file is a sandbox for building an application in prompt toolkit.
'''

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

inst_list = ['Hi-Hat', 'Snare', 'Kick']
inst_completer= WordCompleter(inst_list, ignore_case=True)

command_completer = WordCompleter(['Add Drumkit',
                                   'Add Instrument',
                                   'Change Instrument Rhythm',
                                   'Delete Instrument'],
                                   ignore_case=True)

def prompt_inst():
    '''
    This function prompts the user for an instrument,
    and then prompts for a new rhythm.
    '''
    inst_entry = prompt("> ", completer=inst_completer) #pass history in here or nah?
    
    if inst_entry in inst_list:
        rs = prompt("Rhythm > ") #pass history in here or nah?
        print(inst_entry,':',rs)
    else:
        print('Enter Hi-Hat, Snare, or Kick')

def change_inst():
    pass

def rm_inst():
    pass

def go():
    history = InMemoryHistory()

    while True:
        try:
            prompt_inst()    
        except EOFError:
            break  # Control-D pressed.

    print('Sweet Beats!')

if __name__ == '__main__':
    go()
