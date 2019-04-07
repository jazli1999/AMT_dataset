import specdataset
import sys

label = sys.argv[1]
cur_dir = sys.argv[2]

print('Analysing spectrogram for midi note ' + str(label) + '....')
specdataset.spec(label, cur_dir)
print('Spectrogram for note ' + label + 'all saved\n')

