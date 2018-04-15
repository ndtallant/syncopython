#!/usr/bin/env python3
'''
Nick Tallant
This file is the main user interaction.
'''
# Shell Functionality
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

# Project Specific
from src.transcription import Transcription 
from src.transcription import RhythmString 
from src.user_messages import load_screen, get_help
from src.synco_2 import MidiOut

inst_list = ['Hi-Hat', 'Snare', 'Kick']



command_completer = WordCompleter(['Add Instrument',
                                   'Change Instrument',
                                   'Delete Instrument',
                                   'See Drumkit',
                                   'help', 'exit', 'play'],
                                   ignore_case=True)

def prompt_inst(comp_list=inst_list, no_rhythm=False):
    '''
    This function prompts the user for an instrument,
    and then prompts for a new rhythm.
    '''
    r = RhythmString()
    comp= WordCompleter(inst_list, ignore_case=True)
    
    while True:    
        
        inst_entry = prompt("   Instrument > ", completer=comp) #pass history in here or nah?

        if inst_entry in comp_list:
            if no_rhythm:
                return inst_entry   
            rhy = prompt_rhythm()       
            break
      
        else:
            print('\nPlease Enter one of the following: ') 
            for option in comp_list:
                print(option)
            print('\n')
    
    r.label = inst_entry
    r.rhythm = rhy
    r.set_patch()
    return r 
    
def prompt_rhythm():
    '''Prompts the user for a rhythm, put error handling here maybe'''
    return prompt("     Rhythm > ") 
     
def change_inst(rm_inst=False):
    '''
    Will update the transcription stack and overwrite an instrument.
    '''
    raise NotImplementedError 

def del_inst(t):
    '''Deletes an Instrument from the Stack'''
    del_completer = [inst.label for inst in t.stack]
    if del_completer:
        print('What instrument to you want to remove?') 
        label = prompt_inst(comp_list=del_completer, no_rhythm=True) 
        t.stack = [inst for inst in t.stack if inst.label != label] 
    else:
        print('There are no instruments on your kit yet!')
    return t

def prompt_command(t, action):
    '''Interface for user to enter commands in command completer.'''
    
    command = prompt("> ", completer=command_completer) 

    if command == 'Add Instrument':
        t.stack.append(prompt_inst())

    if command == 'Change Instrument':
        t = change_inst()
 
    if command == 'Delete Instrument':
        t = del_inst(t)

    if command in {'play', 'exit', 'help'}:
        action = command 

    if command == 'See Drumkit':
        try: 
            for inst in t.stack:
                print(inst)
            
            if len(t.stack) == 0:
                print('There are no instruments on your kit!')
        
        except: # I know...
            print('I can\'t see a drumset right now')
            print('Dev-note: no Transcription stack')

    return t, action

if __name__ == '__main__':
    
    load_screen()
    history = InMemoryHistory()
    t = Transcription() 
    while True:
        try:
            action = None 
            t, action = prompt_command(t, action)    
            
            if action == 'help':
                get_help()
            
            if action == 'play':
                with MidiOut(t=t, user_port='1') as out:
                    out.play()
            
            if action == 'exit':
                break 
        
        except EOFError:
            break  # Control-D pressed.
    
    print('\nSweet Beats!\n')
