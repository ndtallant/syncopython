#!/usr/bin/env python3
'''
This file is a sandbox to learn prompt_toolkit.
The goal is to have a two paned/windowed full
screen application.
'''
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.application import Application
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding.manager import KeyBindingManager
from shell_app import prompt_a_drummer

manager = KeyBindingManager()
registry = manager.registry

@registry.add_binding(Keys.ControlQ, eager=True) #eager as False may delay event?
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `CommandLineInterface.run()` call.
    """
    event.cli.set_return_value(None)



if __name__ == "__main__":
    loop = create_eventloop()
    application = Application(key_bindings_registry=registry,
                              use_alternate_screen=True)
        ''' 
            Default Settings of application instance:
                - exit & abort raise exception 
                - no buffers
                - on_input_timeout – Called when there is no input for x seconds. 
                - on_start – Called when reading input starts.
                - on_stop – Called when reading input ends.
                - on_reset – Called during reset.
                - on_buffer_changed – Called when the content of a buffer has been changed.
                - on_initialize – Called after the CommandLineInterface initializes.
                - on_render – Called right after rendering.
                - on_invalidate – Called when the UI has been invalidated.
        ''' 
        
    cli = Commface(application=application, 
                       eventloop=loop)
                          # input=prompt_a_drummer())
    
        ''' 
            cli input needs to be an Input type (std in?)
            Plugging in the prompt sequence as an event
            is the missing piece. Maybe in loop? 
        '''

    cli.run()
    print('Exiting')
