import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

def analyze_uc_peaks(data):
    uc_values = data['Uc(TOCO)'].values
    time_values = data['Time(ms)'].values

    peaks, _ = find_peaks(uc_values, height=10)
    results_half = peak_widths(uc_values, peaks, rel_height=0.5)
    peak_widths_ms = results_half[0] * 250
    
    wide_peaks = peak_widths_ms[peak_widths_ms > 30000]
    
    avg_wide_peak_duration = np.mean(wide_peaks) if len(wide_peaks) > 0 else 0
    print(f"Number of UC peaks wider than 30 seconds: {len(wide_peaks)}")
    print(f"Average duration of UC peaks wider than 30 seconds: {avg_wide_peak_duration:.2f} milliseconds")
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_values, uc_values, label='UC (TOCO)', color='blue')
    plt.plot(time_values[peaks], uc_values[peaks], 'rx', label='Detected Peaks')
    plt.title('UC (TOCO) Signal with Detected Peaks')
    plt.xlabel('Time (ms)')
    plt.ylabel('UC (TOCO)')
    plt.legend()
    plt.show()
