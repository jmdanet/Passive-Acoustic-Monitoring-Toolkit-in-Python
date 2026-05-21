# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:06:29 2026

@author: UP60047104
"""

import soundfile as sf

# Chemin vers ton fichier FLAC
file_path = "FO-S03.mp3"

# Lecture du fichier
data, samplerate = sf.read(file_path)

# Nombre total d'échantillons
n_samples = data.shape[0]

# Durée totale en secondes
duration_seconds = n_samples / samplerate

print("=== Informations du fichier acoustique ===")
print(f"Fréquence d'échantillonnage : {samplerate} Hz")
print(f"Nombre total d'échantillons : {n_samples}")
print(f"Durée totale : {duration_seconds:.2f} secondes")
print(f"Durée totale : {duration_seconds/60:.2f} minutes")
