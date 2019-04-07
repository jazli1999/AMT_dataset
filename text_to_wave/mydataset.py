'melo_midi_wave'

__author__ = 'jasli'

import os
import sys
import math

NOTES = {'60':'C', '62':'D', '64':'E', '65':'F', '67':'G', '69':'A'}

def melo_text_gen(midi_note):
	print('generating melo files for midi note ' + midi_note + '....')

	TEXT_PATH = './text/' + midi_note + '/'
	TONE_NUM = 14
	VOL_STEP = 20
	NOTE_VALUE = 4
	CUR_NOTE = NOTES[midi_note] 


	tones = [4, 5, 24, 25, 26, 27, 36, 37, 38, 39, 40, 42, 73, 78]
	file_count = 1

	os.system('rm -f -r TEXT_PATH')
	os.makedirs(TEXT_PATH)

	for vol in range(47, 154, VOL_STEP):
		for tone in tones:
			for value in range(0, NOTE_VALUE):
				
				title = 'title: mono\n'
				comp = 'composer: Jasli\n'
				beats = 'beats: 4\n'
				tempo = 'tempo: 120\n\n'
				filename = str(file_count) +'.melo'
			
				voice_block = '\tprogram: ' + str(tone) + '\n\tchannel: 1\n\toctave: 0\n\tvolume: ' + str(vol)
				voice = 'voice Mono\n{\n' + voice_block + '\n}\n\n'
			
				play_block = 'play Mono\n{\n\t:|' + CUR_NOTE

				for i in range(0, int(math.pow(2,value)-1)):
					play_block = play_block + '-'
				
				play_block = play_block + '|\n}\n'

				with open(TEXT_PATH + filename, 'w') as f:
					f.write(title + comp + beats + tempo)
					f.write(voice)
					f.write(play_block)
				
				file_count += 1;

	print(str(file_count-1) + 'melo files generated\n')


def text_to_midi(midi_note):
	print('Compiling melo files of midi note ' + midi_note + ' to midi files....')

	TEXT_PATH = './text/' + midi_note + '/'
	MIDI_PATH = './midi/' + midi_note + '/'

	os.makedirs(MIDI_PATH)

	text_files = os.listdir(TEXT_PATH)
	for text in text_files:
		text_file = TEXT_PATH + text
		midi_file = MIDI_PATH + text.split('.')[0] + '.mid'
		os.system('melo mid ' + text_file + ' --output ' + midi_file + ' > /dev/null 2>&1')

	print('All melo files complied\n')


def midi_to_wave(midi_note):
	print('Converting midi files of midi note ' + midi_note + ' to wave files....')

	MIDI_PATH = './midi/' + midi_note + '/'
	AUDIO_PATH = './audio/' + midi_note + '/'
	
	os.makedirs(AUDIO_PATH)

	midi_files = os.listdir(MIDI_PATH)
	for midi in midi_files:
		wave = midi.split('.')[0] + '.wav'
		os.system('timidity -Ow \"./midi/' + midi_note + '/' + midi + '\" -o \"./audio/' + midi_note + '/' + wave + '\" > /dev/null')

	print('All midi file converted\n')


def dataset_gen(midi_note):
	print('generating mid&wav dataset for midi note ' + midi_note + '....\n')
	
	melo_text_gen(midi_note)
	text_to_midi(midi_note)
	midi_to_wave(midi_note)
	
	print('dataset generated\n')


if __name__ == '__main__':
	if len(sys.argv) == 1:
		dataset_gen('60')
	else:
		dataset_gen(sys.argv[1])
	# test as midi note C4
