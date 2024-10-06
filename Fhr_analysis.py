import numpy as np

def analyze_fhr_epochs(data, epoch_duration=3.75):
    epoch_size = int(epoch_duration / 0.25)
    fhr_values = data['Fhr1(BPM)'].values
    num_epochs = len(fhr_values) // epoch_size

    avg_fhr_bpm = []
    avg_fhr_pulse_interval = []

    for i in range(num_epochs):
        epoch_fhr = fhr_values[i * epoch_size : (i + 1) * epoch_size]
        avg_bpm = np.mean(epoch_fhr)
        avg_pulse_interval = (60 * 1000) / avg_bpm
        avg_fhr_bpm.append(avg_bpm)
        avg_fhr_pulse_interval.append(avg_pulse_interval)

    return avg_fhr_bpm, avg_fhr_pulse_interval
