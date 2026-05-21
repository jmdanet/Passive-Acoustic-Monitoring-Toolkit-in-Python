# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:26:26 2026

@author: UP60047104
"""

import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

file_path = "4083.mp3"
signal, fs = sf.read(file_path)
if signal.ndim > 1:
    signal = signal[:, 0]

# Segment de 5 minutes
segment_minutes = 5
segment_seconds = segment_minutes * 60
start_time = 0
start_sample = int(start_time * fs)
end_sample = start_sample + int(segment_seconds * fs)
segment = signal[start_sample:end_sample]

# Spectrogramme
nperseg = fs * 2
noverlap = fs

f, t, Sxx = spectrogram(segment, fs=fs, window='hann', nperseg=nperseg, noverlap=noverlap, scaling='density', mode='psd')
Sxx_dB = 10 * np.log10(Sxx + 1e-12)

# Seuil en dB pour mettre en évidence les événements
seuil_dB = np.median(Sxx_dB) + 12  # +6 dB au-dessus de la médiane
Sxx_events = np.where(Sxx_dB > seuil_dB, Sxx_dB, np.nan)

# Affichage
plt.figure(figsize=(12,5))
plt.pcolormesh(t, f, Sxx_events, shading='gouraud', cmap='inferno')
plt.colorbar(label='PSD (dB re 1µPa²/Hz)')
plt.xlabel('Temps (s)')
plt.ylabel('Fréquence (Hz)')
plt.title(f'Événements acoustiques (segment de {segment_minutes} min)')
plt.ylim(0, fs/2)
plt.tight_layout()
plt.show()

# Filtrer la bande 0–500 Hz
mask = f <= 2500
Sxx_low = np.where(mask[:, None], Sxx_dB, np.nan)

plt.figure(figsize=(12,5))
plt.pcolormesh(t, f, Sxx_low, shading='gouraud', cmap='inferno')
plt.colorbar(label='PSD (dB)')
plt.xlabel('Temps (s)')
plt.ylabel('Fréquence (Hz)')
plt.title('Bande basse : bruit possible de navire')
plt.ylim(0, 2500)
plt.show()

