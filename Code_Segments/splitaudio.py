# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 02:06:47 2022

@author: Yap
"""

from pydub import AudioSegment
import math


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
        t1 = from_min  * 1000  #* 60 if 1 min
        t2 = to_min * 1000 #* 60 if 1 min
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration()) #here divide if you want only a segment of full duration
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
                
#execution
folder = 'C:/Users/username/Folder' 
file = 'audiofilename.wav'
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)
