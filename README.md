# syncopython
A python module for rhythm production.
Read about the development process [here](https://syncopython.blog/).

## Installation
Install dependent packages by running:

```
pip3 install -r requirements.txt
```

from the top level directory (preferably in a virtual environment).

See how to get all dependencies set for sound [here](https://github.com/ndtallant/syncopython/blob/master/get_sound.md).

## Required Modules

* attrs
* pluggy
* pytest
* python-rtmidi
* rtmidi
* six
* [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/index.html)
* [docopt](http://docopt.org/)   

## Functionality 
syncopython is an interactive shell application with two distinct modes

#### 1. Freestyle Mode
This mode prompts the user to create a single bar drum beat using [standard counting](#notation), which is played through the speakers as a live-loop. The user can then update the drumbeat in real time.

##### Developer To-do
1. ~~Have prompt take in notation and play the beat back.~~ 
2. Have the user be able to update beat through prompt.
    - Find a way for MidiOut class to run without overtaking the shell.
    - Have sequencer know when to quit and be replaced with new one. 
3. Have a second pane to display output (general output for now, nothing fancy)
    - Bonus: output in MusicXML

#### 2. Song Mode
This mode allows the user to create a song by first prompting for the form of the song in sections (Example: ABAB), and then prompts the user for each bar in the section. 

##### Developer To-do
1. ~~Have prompt take in notation and play the beat back.~~ 
2. Have the sequencer know when to stop at the end of a section.
3. Have control flow queue up sections to the sequencer correctly.
4. Have a second pane to display output specific to section.
    - Bonus: output full song in MusicXML
- reorder sections

#### Current Feature Limitations
Currently I am stuck in the 4/4 time signature with a single dynamic.

Contribute
---------
- [Submit an Issue](https://github.com/ndtallant/syncopython/issues)
- [Source Code] (https://github.com/ndtallant/syncopython)
