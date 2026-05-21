# Passive Acoustic Monitoring Toolkit

Python toolkit for passive acoustic analysis using spectrograms and signal processing.

## Overview

This project provides simple tools for:

* audio file inspection;
* spectrogram generation;
* acoustic event detection;
* low-frequency noise analysis;
* template-based pattern recognition using 2D correlation.

The toolkit is designed for environmental acoustics, passive sonar, bioacoustics, and maritime monitoring applications.

---

## Features

### Audio Inspection

* Read audio files (`MP3`, `WAV`, `FLAC`)
* Display:

  * sampling rate
  * duration
  * number of channels
  * signal statistics

### Spectrogram Analysis

* Generate spectrograms using `scipy.signal.spectrogram`
* Convert power spectral density to decibels
* Visualize acoustic activity over time

### Acoustic Event Detection

* Detect high-energy acoustic events
* Thresholding based on median energy
* Highlight transient or abnormal sounds

### Low Frequency Analysis

* Focus on low-frequency bands
* Useful for:

  * ship noise detection
  * engine monitoring
  * underwater acoustics

### Pattern Recognition

Template-based acoustic pattern detection using 2D correlation.

Implemented templates:

* impulsive clicks
* chirps / glissandos
* tonal signals
* continuous noise
* harmonic structures
* repeated trills
* modulated impulses

---

## Technologies

* Python 3
* NumPy
* SciPy
* Matplotlib
* SoundFile

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/passive-acoustic-toolkit.git
cd passive-acoustic-toolkit
```

Install dependencies:

```bash
pip install numpy scipy matplotlib soundfile
```

---

## Example Usage

### Audio Information

```python
python audio_info.py
```

### Spectrogram and Event Detection

```python
python spectrogram_analysis.py
```

### Pattern Recognition

```python
python pattern_matching.py
```

---

## Project Structure

```text
passive-acoustic-toolkit/
│
├── audio_info.py
├── spectrogram_analysis.py
├── pattern_matching.py
├── data/
├── outputs/
└── README.md
```

---

## Applications

* Passive acoustic monitoring
* Maritime surveillance
* Ship noise analysis
* Bioacoustics
* Environmental monitoring
* Underwater acoustics
* Signal processing education

---

## Future Improvements

* Real-time processing
* Machine learning classification
* CNN-based spectrogram recognition
* Automatic event extraction
* CSV/JSON export
* Interactive dashboard
* Batch processing

---

## Author

Jean-Marie Danet

---

## License

none
