# Getting Sound Dependencies Set
[This document largely follows this, Thanks Ted!](http://tedfelix.com/linux/linux-midi.html)

### Install Ubuntu (virtual env)
16.04 xenial

## Low Latency Kernel Installation
`$ uname -a`

If "PREEMPT" is not in the output, run
`$ sudo apt-get install linux-lowlatency`

## JACK and "audio groups"

First install [JACK](http://www.jackaudio.org/faq/about.html)

`$ sudo apt-get install jackd2`

Say yes when it asks for real time privileges.

`$ sudo apt install libjack-jackd2-dev`

Check to see if you are in the audio group by running,
`groups | grep audio`. If nothing comes back, enter

`$ sudo gpasswd -a <username> audio`

**reboot**

## ALSA and your sound card
Check to see what ALSA thinks your sound hardware is.

`$ cat /proc/asound/cards`

Your ALSA device name will be "hw:n,m", where n is the number associated with your sound card from above, and m is the number associated with a subdevice. Check for subdevices with

`aplay -l`

Hopefully your system will use "hw:0" - meaning ALSA sees your sound card as the first entry with no subdevices. If you have many sound cards, you may find [this](http://www.alsa-project.org/main/index.php/Asoundrc) helpful.

*note*: /proc is a directory that contains virtual files with info about your system. Neat!

## Test ALSA with a wav file

Use sox (SOund eXchange) to create a wav file.

`$ sudo apt-get install sox`

`$ sox -b 16 -n test.wav rate 48000 channels 2 synth 1 sine 440 gain -1`

`$ aplay -D hw:0 test.wav`

### Other ALSA tidbits

`$ sudo apt install libasound2-dev` (we'll need this for rtmidi later)

## Installing a soft synth
*Many guides I found used fluidsynth, however that broke my machine*

We can use:
* [tiMidity](https://github.com/geofft/timidity): a soft synth
* [pmidi](http://www.parabola.me.uk/alsa/pmidi.html): command line program to run MIDI through ALSA

`$ sudo apt-get install timidity`

`$ sudo apt install pmidi`

### Playing MIDI through the synth
Download a MIDI file like [this download](http://www.midiworld.com/download/4040).

`$ pmidi -l` (this will list off available ports)

Using a port from that output, play a MIDI file:

`$ pmidi -p <number:number for a tiMidity port> <file.mid>`

<!---
# Fluidsynth broke my machine:
check back later lol

 We'll start with fluid synth:

`$ sudo apt-get install fluidsynth`
`$ sudo apt-get install fluid-soundfont-gm`

`fluid-soundfont-gm` may already be installed with `fluidsynth`

Reading for [sound fonts](https://en.wikipedia.org/wiki/SoundFont) and [General MIDI](https://en.wikipedia.org/wiki/General_MIDI) --->

# Getting Python Dependencies
Many things aren't installed with a fresh install of Ubuntu!

`$ sudo apt-get upgrade python3`

`$ sudo apt install python3-pip`

`$ pip3 install --upgrade pip`

`$ sudo pip3 install mido`

`$ sudo pip3 install Cython`

`$ sudo pip3 install rtmidi`

`$ sudo pip3 install python-rtmidi`

## Playing a MIDI file through mido

I only got this to work in a very specfic way - need to figure out why it works this way.

* open interpreter
* import mido
* cd /mido/examples/midifiles (git repo)
* run play_midi_file.py <file> 'tiMiditiy port 0'

The port name was found using list_ports.py. Other tiMidity ports worked.

### Sound test checklist

1. Check midi file plays natively with pmidi (above)
2. drumseq sequencer plays natively
  * run server?
