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

*note*: /proc is a directory that contains virtual files whit info about your system. Neat!

## Test ALSA with a wav file

Use sox (SOund eXchange) to create a wav file.

`$ sudo apt-get install sox`

`$ sox -b 16 -n test.wav rate 48000 channels 2 synth 1 sine 440 gain -1`

`$ aplay -D hw:0 test.wav`
