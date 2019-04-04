
'Compile melo file to midi file'

__author__ = 'jasli'

import sys
import os

NOTE = sys.argv[1]

TEXT_PATH = './text/' + NOTE + '/'
MIDI_PATH = './midi/' + NOTE + '/'

os.makedirs(MIDI_PATH)

text_files = os.listdir(TEXT_PATH)
for text in text_files:
	text_file = TEXT_PATH + text
	midi_file = MIDI_PATH + text.split('.')[0] + '.mid'
	os.system('melo mid ' + text_file + ' --output ' + midi_file)
