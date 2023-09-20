import numpy as np
import matplotlib.pyplot as plt

import librosa
import soundfile as sf
import os



'''
    =======================
    Input test signal
    =======================
'''
input_signal = np.zeros(1000)

for i in range(200):
    input_signal[i] = 1
    input_signal[i+200] = -1



'''
    =======================
    Parameters
    =======================
'''

alpha = 0.95
beta = 0.988


'''
    =======================
    Filters
    =======================
'''

def filter_alpha(input_signal, alpha):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        y[i+1] = input_signal[i+1] + alpha * (y[i] - input_signal[i+1])
    return y


def filter_beta(input_signal, beta):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        y[i+1] = max(input_signal[i+1], beta * y[i])
    return y



output_signal = filter_alpha(filter_beta(input_signal, beta), alpha)

# plot images: input signal + filtered signal
plt.plot(input_signal, color='g', label='Input')
plt.plot(output_signal, color='r', label='Output')
plt.legend()
plt.show()










'''
# importing an audio file
folder_address = '/Users/cookie/dev/filter_designer/test_audio_files/'
destination_address = '/Users/cookie/dev/filter_designer/filter_results/'

file = 'ba-dum-bum-all-74740.wav'
audio_file = folder_address + file
input_signal_wav, sample_rate = librosa.load(audio_file)


output_signal_wav = filter_alpha(filter_beta(input_signal_wav, beta), alpha)
sf.write(destination_address+file, output_signal, sample_rate)
'''