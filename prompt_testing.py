#!/usr/bin/env python3
'''
Nick Tallant
This file is a sandbox for building an application in prompt toolkit.
'''

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

instrumentation = WordCompleter(['Hi-Hat', 'Snare', 'Kick'], ignore_case=True)

def main():
    history = InMemoryHistory()

    while True:
        text = prompt("> ", history=history, completer=instrumentation)
        print('You entered:', text)
    print('GoodBye!')

if __name__ == '__main__':
    main()
