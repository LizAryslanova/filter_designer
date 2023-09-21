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

a = 0.8
b = 0.2
g = 0.9
d_a = 0.9
d_r = 0.1


'''
    =======================
    Filters
    =======================
'''

def symmetric_filter(input_signal, alpha):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        y[i+1] = input_signal[i+1] + alpha * (y[i] - input_signal[i+1])
    return y


def release_filter(input_signal, alpha):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        y[i+1] = input_signal[i+1] + max(0, alpha * (y[i] - input_signal[i+1]))
    return y

def attack_filter(input_signal, alpha):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        y[i+1] = input_signal[i+1] + min(0, alpha * (y[i] - input_signal[i+1]))
    return y


def c_ballistic_filter(input_signal, alpha_attack, alpha_release):
    y = np.zeros(len(input_signal))
    for i in range(len(input_signal) - 1):
        if input_signal[i+1] <= y[i]:
            alpha = alpha_attack
        else:
            alpha = alpha_release

        y[i+1] = input_signal[i+1] + alpha * (y[i] - input_signal[i+1])
    return y




output_signal = symmetric_filter(attack_filter(c_ballistic_filter(input_signal, d_a, d_r), g), a)

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