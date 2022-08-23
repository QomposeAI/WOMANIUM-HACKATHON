# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:40:07 2022

@author: Bengisu

video processer
"""
import os
import csv
import math
from flask import Flask # request
from dss_0 import Disfluency_Spotting_Service
from splitwavaudiobin import SplitWavAudioMubin

LOAD_MODEL = "SE-ResNet_for_disfluency.hdf5"

NUM_SAMPLES_TO_CONSIDER = 16000
 
app = Flask(__name__)

@app.route("/predict", methodas= ["POST"])


def cut_predict(folder, file, filename):
    
    #folder = 'C:/Users/Yap/Downloads/Qompose.AI/splitAudio' 
    #file = 'demogecko.wav'
    #filename = 'demogecko.wav'
    
    swam = SplitWavAudioMubin(file) #splitwavaudiobin.py
    dss = Disfluency_Spotting_Service() #dss_0.py
    
    total_dur = math.ceil(swam.get_duration())
    min_per_split = 1  #its written as min but it actually corresponds to duration of clips wished to be in seconds
    
    
    
    for i in range(0, total_dur, min_per_split):  #total duration is the duration of the audio uploaded
            split_fn = str(i) + '_' + filename #its name the wav is saved
            swam.single_split(i, i + min_per_split , split_fn) #i this command also saves the clips 
            print(str(i) + ' Done')
            
            audio_file = split_fn
            #audio_file = request.files["split_fn"] # i dont think request is needed since the clip is saved internally but still here incase #this is for ai so in "file" the clip which was saved is inserted
            
            second_interval = i, i + min_per_split #this is for the cvs file which will save the seconds info       
            
            predicted_keyword = dss.predict(split_fn) #prediction made by ai
            
            data = [i, audio_file, second_interval, predicted_keyword]
            os.remove(audio_file)
            with open("video_seconds_labels.csv", mode = "a", newline='' ) as f:  
                
                    #data = [i, audio_file, second_interval, predicted_keyword]
                    csv_writer = csv.writer(f, delimiter = ",")
                    csv_writer.writerow(data)              
                
            if i == total_dur - min_per_split: #for loop to stop when it reaches the end
                print('All done successfully')
                break
                               
                
            
            
           
                  
                  
                       
    
    
    































