# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 07:08:12 2022

@author: Yap
"""

import librosa #python librosa install needed
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def callspec():
    file = "static/uploads/audio/extracted_audio.wav" #define path audio file

    test, sr = librosa.load(file,sr=16000) #librosa audioload

    FRAME_SIZE = 400 #define params for stft these are optimal for 16000
    HOP_SIZE = 160

    def plot_spectrogram(spec, sr, hop_length, y_axis="linear"): # the plotting function can change params here
        plt.figure(figsize=(19, 1.25))
        librosa.display.specshow(spec, 
                                sr=sr, 
                                hop_length=hop_length, 
                                x_axis="time", 
                                y_axis=y_axis, cmap='viridis' ) # change color with cmap change plot size with fig size
        #plt.colorbar(format="%+2.f") this can be uncommented it shows the colorbar info

    #here i do the stft to the audio file
    file = librosa.stft(test, n_fft=FRAME_SIZE, hop_length=HOP_SIZE) 
    Y_test = librosa.power_to_db(np.abs(file) ** 2) #increase amplitude in db for bettew view
    plot_spectrogram(Y_test, sr, HOP_SIZE,y_axis='log') #here's freq view remove y_axis='log for linear view
    plt.savefig('sp_xyz.jpg', dpi=300, frameon='true')
