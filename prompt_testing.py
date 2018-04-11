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
instrumentation = WordCompleter(inst_list, ignore_case=True)
 
def main():
    history = InMemoryHistory()

    while True:
        try:
            entry = prompt("> ", history=history, completer=instrumentation)
            
            if entry in inst_list:
                rs = prompt("Rhythm > ", history=history)
                print(entry,':',rs)

            else:
                print('Enter Hi-Hat, Snare, or Kick')

        except EOFError:
            break  # Control-D pressed.

    print('Sweet Beats!')

if __name__ == '__main__':
    main()
