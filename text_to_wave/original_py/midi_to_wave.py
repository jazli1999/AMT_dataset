'Convert midi files to playable wave files'

__author__ = 'jasli'

import os
import sys

NOTE = sys.argv[1]
MIDI_PATH = './midi/' + NOTE + '/'
AUDIO_PATH = './audio/' + NOTE + '/'

midi_files = os.listdir(MIDI_PATH)
for midi in midi_files:
	wave = midi.split('.')[0] + '.wav'
	os.system(u'timidity -Ow "./midi/"' + NOTE + '/' + midi + ' -o ./audio/' + NOTE + '/' + wave)
