from data_loader import load_data, preprocess_data
from plotting import plot_fhr, plot_uc
from Fhr_analysis import analyze_fhr_epochs
from Uc_analysis import analyze_uc_peaks

# Load and preprocess data
data = load_data('path/to/Simulator_readings.csv')  # Replace with your actual file path
data = preprocess_data(data)

# Plot data
plot_fhr(data)
plot_uc(data)

# Analyze FHR and UC
avg_fhr_bpm, avg_fhr_pulse_interval = analyze_fhr_epochs(data)
print("Average FHR (bpm):", avg_fhr_bpm)
print("Average Pulse Interval (ms):", avg_fhr_pulse_interval)

analyze_uc_peaks(data)
