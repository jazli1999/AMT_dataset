import specdataset
import sys

labels = [60, 62, 64, 65, 67, 69]

for label in labels:
	print('Analysing spectrogram for midi note ' + str(label) + '....')
	specdataset.spec(str(label))
	print('Spectrogram for note ' + str(label) + 'all saved\n')
