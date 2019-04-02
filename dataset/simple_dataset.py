import librosa, librosa.display, librosa.util
import matplotlib.pyplot as plt
import numpy as np
import os

img_path = '../dataset/img/60'
audio_path = '../dataset/audio/60'

wav_filenames = os.listdir(audio_path)
for wav_filename in wav_filenames:
    y, sr = librosa.load(audio_path+ '/' +wav_filename)
    img_filename = '/' + (wav_filename.split('.'))[0] + '.png'

    print('CQTing ' + wav_filename + '....')
    C = np.abs(librosa.cqt(y, sr=sr, hop_length=64, n_bins = 84, bins_per_octave = 12))
    librosa.display.specshow(librosa.amplitude_to_db(C), sr=sr, x_axis='time', y_axis='cqt_note')
    print('Drawing ' + wav_filename + '....')
    plt.set_cmap('hot')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(img_path+img_filename, format='png', transparent=False, dpi=300, pad_inches=0)
    print(img_path+img_filename + ' saved')