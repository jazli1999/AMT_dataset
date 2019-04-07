'Generate original melo files'

__author__ = 'jasli'

import sys
import os
import math

NOTE = sys.argv[1]

TEXT_PATH = './text/' + NOTE
TONE_NUM = 14
VOL_STEP = 20
NOTE_VALUE = 4
CUR_NOTE = chr(ord('C') + (int(NOTE)-60)/2)


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
	
