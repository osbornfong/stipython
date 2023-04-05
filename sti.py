#%%
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt

def wav_to_sti(wav_file_path):  
    # File to be read
    #audio_file = './signals/3sectone.wav'
    #audio_file = './signals/lin_sweep_1Hzto24kHz_48kHzSR_10s_signed16bit.wav'

    # Read audio file
    Fs,data = wavfile.read(wav_file_path)

    # Time series data
    data = data.astype(object)
    x = np.linspace(0,len(data),len(data),0)

    plt.figure()    
    plt.plot(x, data)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title("Time Series Data")

    # Spectrum
    spectrum_complex = fft(data)
    spectrum_magnitude = abs(spectrum_complex)

    plt.figure()
    plt.plot(np.linspace(0,len(spectrum_magnitude),len(spectrum_magnitude),0),spectrum_magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title("Frequency Response")

    # Envelope Function
    x = np.linspace(0,len(data),len(data),0)
    envelope_function = data**2

    plt.figure()    
    plt.plot(x, envelope_function)
    plt.xlabel('Sample')
    plt.ylabel('Squared Amplitude')
    plt.title("Envelope Function")

    # Energy
    energy = envelope_function.sum()
    print(energy)

    # Modulation Transfer Function
    # According to Schroeder, the CMTF is the complex Fourier transform of the squared impulse response divided by its total energy.
    cmtf = fft(envelope_function)/energy
    cmtf_real = cmtf.real
    cmtf_imaginary = cmtf.imag
    cmtf_magnitude = abs(cmtf)
    plt.figure()    
    plt.plot(x, cmtf_real)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Real Amplitude')
    plt.title("Envelope Spectrum - Real")
    plt.figure()    
    plt.plot(x, cmtf_imaginary)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Imaginary Amplitude')
    plt.title("Envelope Spectrum - Imaginary")
    plt.figure()    
    plt.plot(x, cmtf_magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title("Modulation Transfer Function")
    plt.show()

def open_file_single():

    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return file_path

if __name__ == '__main__':

    file_path = open_file_single()
    print('File selected:' + file_path)

    wav_to_sti(wav_file_path = file_path)

# %%
