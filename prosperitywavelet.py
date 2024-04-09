# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import wavelet
# from wavelet import FastWaveletTransform, WaveletTransform , getExponent
# df = pd.read_csv("prices_round_1_day_0.csv", delimiter = ";")
# Amethysts = df[df['product']== "AMETHYSTS"]
# Starfruit = df[df['product']=="STARFRUIT"]
# Amethystsbase = 10000
# filtered = Amethysts.iloc[0:100]
# fftr = np.fft.fft(filtered['mid_price'])
# sampling_rate = 1  # Assuming data is uniformly sampled
# frequencies = np.fft.fftfreq(len(filtered['mid_price']), 1 / sampling_rate)  # Frequency values


# plt.plot(filtered['mid_price'])
# plt.plot(frequencies,np.abs(fftr))


# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("prices_round_1_day_0.csv", delimiter=";")
Amethysts = df[df['product'] == "AMETHYSTS"]
filtered = Amethysts.iloc[0:1000]  # Assuming you want to use the first 100 data points

# Compute FFT
fft_result = np.fft.fft(filtered['mid_price'])
n = len(filtered['mid_price'])
sampling_rate = 1  # Assuming data is uniformly sampled
frequencies = np.fft.fftfreq(n, 1 / sampling_rate)  # Frequency values
reconstructed_signal = np.fft.ifft(fft_result)
reconstructed_signal = np.real(reconstructed_signal)  # Take real part of the signal


plt.plot(filtered['timestamp'],(filtered['mid_price']-reconstructed_signal))
print(reconstructed_signal)
print(filtered['mid_price'])
# # Plot both time-domain signal and FFT result
# plt.figure(figsize=(12, 6))

# # Plot time-domain signal
# plt.subplot(1, 2, 1)
# plt.plot(filtered['mid_price'])
# plt.xlabel('Time')
# plt.ylabel('Mid Price')
# plt.title('Time-domain Signal')

# # Plot FFT result (positive frequencies only)
# plt.subplot(1, 2, 2)
# plt.plot(frequencies[:n//2], np.abs(fft_result)[:n//2])  # Plot positive frequencies only
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('FFT of Signal')

# plt.tight_layout()
plt.show()
