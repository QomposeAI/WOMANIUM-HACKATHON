# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:34:38 2022

@author: Bengisu
"""
import tensorflow.keras as keras
import numpy as np
import librosa



LOAD_MODEL = "SE-ResNet_for_disfluency.hdf5"

NUM_SAMPLES_TO_CONSIDER = 16000

class _Disfluency_Spotting_Service:
    
    model = None
    _mappings = [
        "Breath",
        "Laughter",
        "Music",
        "Uh",
        "Um",
        "Words"
    ]
    
    _instance = None
    
    
    
    def preprocess(self, file_path, n_fft = 399, hop_length = 159 ):
        
        # load audio file
        signal, sr = librosa.load(file_path, sr = 16000)
        
        #ensure consistency in audio file length
        if len(signal) > NUM_SAMPLES_TO_CONSIDER:
            signal = signal[:NUM_SAMPLES_TO_CONSIDER]
        
        #extract spectogram
        stft = librosa.stft(signal,
                            n_fft = n_fft,
                            hop_length = hop_length)
        spectogram = np.abs(stft)
        log_spectogram = librosa.amplitude_to_db(spectogram)
        return log_spectogram

    
    
    
    def predict(self, file_path):
        
        #extract septograms
        septograms = self.preprocess(file_path) # (n_bins, n_frames, 1)
        
        #convert 3d sep array into 4d array -- (#samples, #segments, #coefficients, #channels)
        seps = septograms[np.newaxis,..., np.newaxis]
        
        #make prediction
        predictions = self.model.predict(seps) # [ [0.1,0.6, 0.1, ...] ]
        predicted_index = np.argmax(predictions)
        
        predicted_keyword = self._mappings[predicted_index]
        
        return predicted_keyword
    
def Disfluency_Spotting_Service():
    
    
    if _Disfluency_Spotting_Service._instance is None:
        _Disfluency_Spotting_Service._instance = _Disfluency_Spotting_Service()
        _Disfluency_Spotting_Service.model = keras.models.load_model(LOAD_MODEL)
    return _Disfluency_Spotting_Service._instance

"""
#here is for to see if its working
if __name__ == "__main__":
    
    dss = Disfluency_Spotting_Service()
    keyword1 = dss.predict("E:/bengisu/1_ready_to_deploy/2013_Grrrl, Uninterrupted_Ep 3_ Fly, Little Birdie, Fly.wav")
    print(f"predicted keywords: {keyword1}")
"""







