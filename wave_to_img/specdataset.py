'cqt spectrogram transform'

__author__ = 'jasli'

import librosa, librosa.display, librosa.util
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

NOTES = {'60':'C', '62':'D', '64':'E', '65':'F', '67':'G', '69':'A'}

def spec(NOTE, CUR_DIR):
	IMG_PATH = './img/' + NOTE + '/'
	AUDIO_PATH = '../text_to_wave/audio/' + NOTE + '/' + CUR_DIR + '/'
	
	PATH_DB = IMG_PATH + 'db/'
	PATH_AMP = IMG_PATH + 'amp/'

	if bool(1-os.path.exists(IMG_PATH)):
		os.makedirs(IMG_PATH)
	if bool(1-os.path.exists(PATH_DB)):
		os.makedirs(PATH_DB)
	if bool(1-os.path.exists(PATH_AMP)):
		os.makedirs(PATH_AMP)

	wave_files = os.listdir(AUDIO_PATH)
	for wave in wave_files:
		print('processing ' + NOTE + '/' + wave)
		y, sr = librosa.load(AUDIO_PATH + '/' + wave)
		img = (wave.split('.'))[0] + '.png'
		C = np.abs(librosa.cqt(y, sr=sr, hop_length=64, n_bins = 84, bins_per_octave = 12))
		
		librosa.display.specshow(librosa.amplitude_to_db(C), sr=sr, x_axis='time', y_axis='cqt_note')

		plt.set_cmap('hot')
		plt.gca().xaxis.set_major_locator(plt.NullLocator())
		plt.gca().yaxis.set_major_locator(plt.NullLocator())
		plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
		plt.margins(0, 0)
		plt.savefig(PATH_DB + img, format='png', transparent=False, dpi=72, pad_inches=0)

		librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='cqt_note')
		
		plt.set_cmap('hot')
		plt.gca().xaxis.set_major_locator(plt.NullLocator())
		plt.gca().yaxis.set_major_locator(plt.NullLocator())
		plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
		plt.margins(0, 0)
		plt.savefig(PATH_AMP + img, format='png', transparent=False, dpi=72, pad_inches=0)
		

	if __name__ == '__main__':
		if len(sys.argv) == 1:
			spec('60')
		elif len(sys.argv) == 2:
			spec(sys.argv[1])
		else:
			spec(sys.argv[1], sys.argv[2])
