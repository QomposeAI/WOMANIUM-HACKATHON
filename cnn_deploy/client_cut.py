# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:05:52 2022

@author: b
"""

#client.py
import requests

URL = "http://0000000/predict"
AUDIO_FILE_PATH = "test/0000.wav"


if __name__ == "__main__":
    #open files
    audio_file = open(AUDIO_FILE_PATH, "rb" )
    #package stuff to send and perform POST request
    values = { "file": (AUDIO_FILE_PATH, audio_file, "audio/wav" )} 
    response = requests.post(URL, FILES = values)
    #idk if requests is also saving the csv file so add a line if need to
    
    