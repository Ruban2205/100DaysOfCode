# Create a program to perform fast Fourier transform (FFT) on a signal.
print("\nRuban Gino Singh - Day 64 of #100DaysOfCode\n")

print("Python program to perform fast fourier transform\n")

import numpy as np
import matplotlib.pyplot as plt

def perform_fft(signal, sampling_rate):
    fft_result = np.fft.fft(signal)
    
    frequencies = np.fft.fftfreq(len(signal), d=1/sampling_rate)
    
    return frequencies, fft_result

def plot_fft_result(frequencies, fft_result):
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, np.abs(fft_result))
    plt.title('FFT Result')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

def main():
    duration = 1.0  # seconds
    sampling_rate = 1000  # Hz
    frequency = 5  # Hz

    t = np.arange(0, duration, 1/sampling_rate)
    signal = np.sin(2 * np.pi * frequency * t)

    frequencies, fft_result = perform_fft(signal, sampling_rate)

    plot_fft_result(frequencies, fft_result)

if __name__ == "__main__":
    main()


# --------------------------------------------------------- #