import librosa

def main():
    #y is the audio time series, it tracks amplitudes of audio signals over time
    y, sr = librosa.load("skyfall_vocals.wav", sr = None, mono= False)

    #if more than one audio channel, 
    if y.ndim > 1:
            y = y[0, :]
            #reassign y to take first channel
    
    pitch_corrected_y = autotune(y, sr)

    filepath = Path("skyfall_vocals.wav")
    output_filepath = filepath.parent/(filepath.stem + "_pitch_corrected.wav")
