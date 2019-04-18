<img align="right" src="logo/logo.jpg" height="200">

# README  
---  
Technical attempts for building our own AMT dataset.  
Repo for personal use, keeping track of all the possible methods, but not the final solution.  

Only works on Linux for it contains pretty much system path operation.  

## Doc  
- [text\_to\_wave](./text_to_wave)  
  Generate [.melo](https://github.com/Mistodon/melo) format files and convert them into .wav files  
- [wave\_to\_img](./wave_to_img)  
  Convert the audio .wav files above into spectrogram .png files.  

## Usage  
For module in each directory mentioned above, there are existed usage example files in the corresponding directory.  
Here is some brief examples and introduction.  

### Generate .melo files & corresponding .wav files  
`mydataset` in /text\_to\_wave is the module for that, the audio files will be saved in a separate folder under the same directory.  
```python  
import mydataset  
mydataset.dataset_gen(str(note))  
```  
Notice that, here the `note` argument is given in the form of midi note numbers, i.e. C4 is given by 60 and D4 is 62.  

### Transform .wav files into CQT spectrogram imgs  
`wave_to_img` in /wave\_to\_img is the module for that, the img files will also be saved in a separate folder under the same directory.  
```python  
import specdataset  
specdataset.spec(note, cur_dir) 
```  
**Before the formal transformation starts, the python file `splitall.py` in directory ./text\_to\_wave must be executed first.**  


Here needs some explaination if you are interested in this detail.  
> While the argument `note` still given by the midi note representation, the `cur_dir` argument, which represents the sub-directory under the audio folder for each note, seems a little redundant.  
> When I tried to process all the note files in one python program, I found the memory was soon used up while the transforming was unfinished yet. After a while, it crashed and the process was killed. So I separate the audio files for each note into 4 folders and take care of 1 each time. Thus the memory will be clean after each audio folder was processed since the program is shut down.  
> `splitall.py` will separate the files into 4 catagories depending on their name. It's not the necceesary way to implement this.  

### About the files haven't been mentioned....  
- wave\_to\_img/spec\_for\_1  
  It's a batch-processing shell script to save my time. It's not elegant to code like that, but since it's not that troublesome.  

- spectrogram/rosa\_cqt.ipynb  
  Jupyter notebook files to display how to export spectrogram using CQT.  


## Dependencies  
two wonderful & easy-to-use program:  
- [librosa - Python library for audio and music analysis](https://github.com/librosa/librosa)  
- [melo - A music notation language and compiler to MIDI](https://github.com/Mistodon/melo)  

![Our logo: TrOctave](logo/logo.jpg)  

