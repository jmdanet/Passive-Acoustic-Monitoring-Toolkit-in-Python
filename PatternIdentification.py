# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:25:28 2026

@author: UP60047104
"""

# -*- coding: utf-8 -*-
"""
Détection automatique de patterns audio simples dans un spectrogramme
"""

import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram, correlate2d

# --- Chargement du fichier ---
file_path = "bateau.mp3"
signal, fs = sf.read(file_path)
if signal.ndim > 1:
    signal = signal[:, 0]

# Segment de 5 minutes
segment_minutes = 5
segment_seconds = segment_minutes * 60
segment = signal[:segment_seconds*fs]

# --- Calcul du spectrogramme ---
nperseg = fs*2
noverlap = fs
f, t, Sxx = spectrogram(segment, fs=fs, window='hann', nperseg=nperseg, noverlap=noverlap, mode='psd')
Sxx_dB = 10*np.log10(Sxx + 1e-12)

# --- Normalisation pour corrélation ---
Sxx_norm = (Sxx_dB - np.mean(Sxx_dB)) / (np.std(Sxx_dB) + 1e-12)

# --- Définition des templates simples ---
def make_template(pattern_type, f, t):
    """Crée un template simplifié pour la corrélation"""
    template = np.zeros((len(f), len(t)))
    if pattern_type == "Click impulsif":
        # Ligne verticale très fine au milieu
        mid = len(t)//2
        template[:, mid] = 1
    elif pattern_type == "Chirp / Glissando":
        # Diagonale du coin bas gauche au coin haut droit
        for i in range(len(t)):
            freq_idx = int(i * len(f) / len(t))
            if freq_idx < len(f):
                template[freq_idx, i] = 1
    elif pattern_type == "Tonal stable":
        # Ligne horizontale dans la bande basse
        freq_idx = len(f)//10
        template[freq_idx, :] = 1
    elif pattern_type == "Bruit continu":
        template[:, :] = 1  # rempli tout
    elif pattern_type == "Bruit impulsif large":
        mid_t = len(t)//2
        mid_f = len(f)//2
        template[mid_f-2:mid_f+2, mid_t-2:mid_t+2] = 1
    elif pattern_type == "Trille / motifs répétés":
        for i in range(0, len(t), 10):
            freq_idx = len(f)//5
            template[freq_idx-2:freq_idx+2, i:i+2] = 1
    elif pattern_type == "Harmoniques multiples":
        for h in range(1,4):
            freq_idx = len(f)//10*h
            template[freq_idx, :] = 1
    elif pattern_type == "Impulsions modulées":
        for i in range(5, len(t), 20):
            freq_idx = len(f)//4
            template[freq_idx-1:freq_idx+1, i:i+3] = 1
    return template

patterns = ["Click impulsif", "Chirp / Glissando", "Tonal stable",
            "Bruit continu", "Bruit impulsif large", "Trille / motifs répétés",
            "Harmoniques multiples", "Impulsions modulées"]

# --- Calcul des corrélations ---
scores = []
for p in patterns:
    template = make_template(p, f, t)
    # normalisation du template
    template_norm = (template - np.mean(template)) / (np.std(template)+1e-12)
    # corrélation 2D
    corr = correlate2d(Sxx_norm, template_norm, mode='valid')
    score = np.max(corr)
    scores.append(score)

# Normalisation en %
scores_percent = 100 * np.array(scores) / np.sum(scores)

# --- Affichage ---
plt.figure(figsize=(10,5))
plt.bar(patterns, scores_percent, color='orange')
plt.ylabel("Pourcentage de corrélation (%)")
plt.title("Correspondance des patterns audio dans le segment")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
