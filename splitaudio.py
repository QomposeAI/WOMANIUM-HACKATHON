# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 02:06:47 2022

@author: Yap
"""

from pydub import AudioSegment
import math
#from pydub.silence import split_on_silence
'''
sound = AudioSegment.from_file("C:/Users/Yap/Downloads/Qompose.AI/demogeckofullaudio.wav", format="wav")
chunks = split_on_silence(
    sound,

    # split on silences longer than 1000ms (1 sec)
    min_silence_len=200,

    # anything under -16 dBFS is considered silence
    silence_thresh=-16, 

    # keep 200 ms of leading/trailing silence
    keep_silence=200
)

# now recombine the chunks so that the parts are at least 90 sec long
target_length = 90 * 1000
output_chunks = [chunks[0]]
for chunk in chunks[1:]:
    if len(output_chunks[-1]) < target_length:
        output_chunks[-1] += chunk
    else:
        # if the last output chunk is longer than the target length,
        # we can start a new one
        output_chunks.append(chunk)

# now your have chunks that are bigger than 90 seconds (except, possibly the last one)
'''

#class for spliting audio into time defined segments
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min  * 1000  #* 60
        t2 = to_min * 1000 #* 60
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration())
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
                
#execution
folder = 'C:/Users/Yap/Downloads/Qompose.AI/splitAudio' 
file = 'demogecko.wav'
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)
