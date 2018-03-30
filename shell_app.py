#!/usr/bin/env python3
# Nick Tallant - syncopython

# project
from transcription import Transcription, RhythmString

# initialization section, creates the app instance (cli is run in main)

from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.application import Application
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys
from prompt_toolkit import prompt

manager = KeyBindingManager()
registry = manager.registry # registry of keyboard shortcuts for application
loop = create_eventloop()

@registry.add_binding(Keys.ControlQ, eager=True)
def exit_(event):
    ''' 
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `CommandLineInterface.run()` call.
    ''' 
    event.cli.set_return_value(None)

application = Application(key_bindings_registry=registry)
cli = CommandLineInterface(application=application, eventloop=loop)

# layout section, the goal to have a left window for entry
# and a right window for viewing the drum beat

from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FillControl, TokenListControl
from prompt_toolkit.layout.dimension import LayoutDimension as D

from pygments.token import Token

layout = VSplit([
    # One window that holds the BufferControl with the default buffer on the
    # left.
    Window(content=BufferControl(buffer_name=DEFAULT_BUFFER)),

    # A vertical line in the middle. We explicitely specify the width, to make
    # sure that the layout engine will not try to divide the whole width by
    # three for all these windows. The `FillControl` will simply fill the whole
    # window by repeating this character.
    Window(width=D.exact(1),
           content=FillControl('|', token=Token.Line)),

    # Display the text 'Hello world' on the right.
    Window(content=TokenListControl(
        get_tokens=lambda cli: [(Token, 'Hello world')])),
])

def prompt_a_drummer():
    '''
    Prompts the user to make a drummer - four
    separate rhythms.
    '''
    hh = prompt('Hi-Hat: ')
    sn = prompt('Snare: ')
    bd = prompt('Kick: ')

    hatRS = RhythmString(42, hh, 'Hi-Hat')
    snRS = RhythmString(38, sn, 'Snare')
    bdRS = RhythmString(36, bd, 'Kick') 
    t = Transcription()
    t.stack = [hatRS, snRS, bdRS]

    out_str = t.output_drumseq()
    print(out_str)

if __name__ == "__main__":
    # don't run until you have an exit method
    #cli.run()
    prompt_a_drummer()
    print('Exiting')
